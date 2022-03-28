# Python program to calculate monthly payment

def monthly_loan(principal, interest_rate, duration):
    """
    :param principal: total loan amount
    :param interest_rate: per cent interest compounded monthly
    :param duration: in years
    :return: monthly payment
    """
    n = duration * 12  # total number of months

    r = interest_rate / (100 * 12)  # interest per month
    monthly_payment = principal * ((r * ((r + 1) ** n)) /(((r + 1) ** n) - 1))  # formula for

    return monthly_payment


if __name__ == "__main__":
    principal = float(input("total loan amount taken: "))
    interest_rate = float(input("annual interest rate applied: "))
    duration = int(input("loan duration in years: "))
    monthly_amount = monthly_loan(principal, interest_rate, duration)
    print(monthly_amount)
