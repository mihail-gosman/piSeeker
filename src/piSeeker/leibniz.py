import decimal
import datetime
import time


def calculate_term(i):
    return (decimal.Decimal('-1') ** decimal.Decimal(str(i))) / (
                decimal.Decimal("2") * decimal.Decimal(str(i)) + decimal.Decimal("1"))


def calculate_pi_series(iterations, precision):
    decimal.getcontext().prec = precision
    series_terms = []
    pi_terms = []
    series_sum = 0

    for i in range(iterations):
        series_sum += calculate_term(i)
        series_terms.append(series_sum)

    for series_sum in series_terms:
        pi_terms.append(4 * series_sum)

    return pi_terms


def get_pi_from_leibniz_series() -> {}:
    try:
        iterations = int(input("Enter the number of iterations for pi calculation: "))
        precision = int(input("Enter the number of decimal places for precision: "))

        if iterations >= 0 or precision >= 0:
            data = []
            timestamp = datetime.datetime.now()
            data.append(f"PiSeeker Benchmarking Test")
            data.append(f"Start time: {datetime.datetime.now()}")
            data.append(f"Pi Calculation Method: The Gregory-Leibniz Series")
            data.append(f"Number of Iterations: {iterations}")
            data.append(f"Decimal precision: {decimal}")

            start_time = time.time()
            series_terms = calculate_pi_series(iterations, precision)
            end_time = time.time()

            delta_time = end_time - start_time

            data.append(f"End time: {datetime.datetime.now()}")
            data.append(f"Execution Time: {delta_time} seconds")
            result = {
                'series_terms': series_terms,
                'data': data
            }
            return result

        else:
            print("Please enter a positive integer.")
            get_pi_from_leibniz_series()

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        get_pi_from_leibniz_series()
