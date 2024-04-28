import decimal
import datetime


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

    try:
        iterations = int(input("Enter the number of iterations for pi calculation: "))
        precision = int(input("Enter the number of decimal places for precision: "))

        if iterations >= 0 or precision >= 0:
            data = []
            timestamp = datetime.datetime.now()
            data.append(f"{timestamp} : Test started\nAlgorithm: Leibniz")
            series_terms = calculate_pi_series(iterations, precision)
            data.append(f"{timestamp}: Test completed")
            data.append(f"Terms calculated: {series_terms}")

        else:
            print("Please enter a positive integer.")
            get_pi_from_leibniz_series()

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        get_pi_from_leibniz_series()
