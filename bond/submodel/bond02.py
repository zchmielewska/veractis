from cashflower import assign, ModelVariable

from bond.input import policy, runplan
from bond.utils.utils import get_end_date, end_date_to_months


# Input
NOMINAL = 1000
COUPON = 0.02
TERM = 120

START_YEAR = 2022
START_MONTH = 6

# Interest rate
i = 0.02

# Derived attributes
END_YEAR, END_MONTH = get_end_date(START_YEAR, START_MONTH, TERM)
T_END = end_date_to_months(END_YEAR, END_MONTH, runplan.get("valuation_year"), runplan.get("valuation_month"))


# Model to calculate present value of cash flows
cal_month = ModelVariable(modelpoint=policy)
cal_year = ModelVariable(modelpoint=policy)
bond02_cf = ModelVariable(modelpoint=policy)
bond02_pv = ModelVariable(modelpoint=policy)


@assign(cal_month)
def cal_month_formula(t):
    if t == 0:
        return runplan.get("valuation_month")
    if cal_month(t-1) == 12:
        return 1
    else:
        return cal_month(t-1) + 1


@assign(cal_year)
def cal_year_formula(t):
    if t == 0:
        return runplan.get("valuation_year")
    if cal_month(t-1) == 12:
        return cal_year(t-1) + 1
    else:
        return cal_year(t-1)


@assign(bond02_cf)
def bond02_cf_formula(t):
    cf = 0
    # Coupon
    if t != 0 and t <= T_END and cal_month(t) == START_MONTH:
        cf += NOMINAL * COUPON
    # Nominal value
    if t == T_END:
        cf += NOMINAL
    return cf


@assign(bond02_pv)
def bond02_pv_formula(t):
    return round(bond02_cf(t) + bond02_pv(t+1) * (1/(1+i))**(1/12), 2)
