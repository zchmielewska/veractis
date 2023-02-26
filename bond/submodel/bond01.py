from cashflower import assign, ModelVariable

from bond.input import policy


# Input
NOMINAL = 1000
COUPON = 0.02
TERM = 120

# Interest rate
i = 0.02


# Model to calculate present value of cash flows
bond01_cf = ModelVariable(modelpoint=policy)
bond01_pv = ModelVariable(modelpoint=policy)


@assign(bond01_cf)
def bond01_cf_formula(t):
    cf = 0
    # Coupon
    if t != 0 and t <= TERM and t % 12 == 0:
        cf += NOMINAL * COUPON
    # Nominal value
    if t == TERM:
        cf += NOMINAL
    return cf


@assign(bond01_pv)
def bond01_pv_formula(t):
    return round(bond01_cf(t) + bond01_pv(t+1) * (1/(1+i))**(1/12), 2)
