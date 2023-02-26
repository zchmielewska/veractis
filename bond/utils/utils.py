def get_end_date(start_year, start_month, term):
    years = term // 12
    months = term - years * 12

    end_year = start_year + years
    end_month = start_month + months

    if end_month > 12:
        end_year += 1
        end_month -= 12

    return end_year, end_month


def end_date_to_months(end_year, end_month, valuation_year, valuation_month):
    return (end_year - valuation_year) * 12 + (end_month - valuation_month)
