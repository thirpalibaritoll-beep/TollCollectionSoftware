# ============================================
# Toll Collection Software
# calculations.py
# ============================================

def to_float(value):
    """
    Convert textbox value to float.
    Empty or invalid values become 0.
    """
    try:
        if value == "":
            return 0
        return float(value)
    except:
        return 0


# --------------------------------------------
# Total Cash
# --------------------------------------------
def total_cash(a_cash, b_cash, c_cash):
    return (
        to_float(a_cash)
        + to_float(b_cash)
        + to_float(c_cash)
    )


# --------------------------------------------
# Total UPI
# --------------------------------------------
def total_upi(a_upi, b_upi, c_upi):
    return (
        to_float(a_upi)
        + to_float(b_upi)
        + to_float(c_upi)
    )


# --------------------------------------------
# Annual Pass Amount
# Single × 65
# Return × 30
# --------------------------------------------
def annual_pass_amount(single_pass, return_pass):

    single_amount = to_float(single_pass) * 65

    return_amount = to_float(return_pass) * 30

    return single_amount + return_amount


# --------------------------------------------
# Total Collection
# --------------------------------------------
def total_collection(
    cash,
    upi,
    monthly_pass,
    etc_collection,
    annual_amount
):

    return (
        to_float(cash)
        + to_float(upi)
        + to_float(monthly_pass)
        + to_float(etc_collection)
        + to_float(annual_amount)
    )


# --------------------------------------------
# TCS
# --------------------------------------------
def tcs(remittance):
    return round(to_float(remittance) * 0.02, 2)


# --------------------------------------------
# UPI TCS
# --------------------------------------------
def upi_tcs(upi_penalty):
    return round(to_float(upi_penalty) * 0.02, 2)


# --------------------------------------------
# Total Remittance
# --------------------------------------------
def total_remittance(
    remittance,
    tcs_amount,
    upi_penalty,
    upi_tcs_amount
):

    return (
        to_float(remittance)
        + to_float(tcs_amount)
        + to_float(upi_penalty)
        + to_float(upi_tcs_amount)
    )


# --------------------------------------------
# Total Expense
# --------------------------------------------
def total_expense(expense_list):

    total = 0

    for amount in expense_list:

        total += to_float(amount)

    return total


# --------------------------------------------
# Profit / Loss
# --------------------------------------------
def profit_loss(
    collection,
    remittance,
    expense
):

    return (
        to_float(collection)
        - to_float(remittance)
        - to_float(expense)
    )