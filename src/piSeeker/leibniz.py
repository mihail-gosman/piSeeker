import decimal
from src.piSeeker import datalog


def calculate_termen(i):
    return (decimal.Decimal('-1') ** decimal.Decimal(str(i))) / (
                decimal.Decimal("2") * decimal.Decimal(str(i)) + decimal.Decimal("1"))


def calculate_pi_series(iterations, precision):
    decimal.getcontext().prec = precision
    series_terms = []
    pi_terms = []
    term = 0

    for i in range(iterations):
        term += calculate_termen(i)
        series_terms.append(term)

    for term in series_terms:
        pi_terms.append(4 * term)

    return pi_terms


def get_pi_from_leibniz_series():
    data_logger = datalog.DataLogger()

    try:
        iterations = int(input("Enter the number of iterations for pi calculation: "))
        precision = int(input("Enter the number of decimal places for precision: "))

        if iterations >= 0 or precision >= 0:
            series_terms = calculate_pi_series(iterations, precision)


        else:
            print("Please enter a positive integer.")
            del data_logger
            get_pi_from_leibniz_series()


    except ValueError:
        print("Invalid input. Please enter a valid integer.")
