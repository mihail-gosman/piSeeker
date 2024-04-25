import decimal


def calculate_pi_series(iterations, precision):
    decimal.getcontext().prec = precision
    series_terms = []
    current_term = decimal.Decimal()

    for i in range(iterations):
        current_term = (decimal.Decimal('-1') ** decimal.Decimal(str(i))) / (decimal.Decimal("2") * decimal.Decimal(str(i)) + decimal.Decimal("1"))
        series_terms.append(current_term)

    approx_pi = 0
    for term in series_terms:
        approx_pi += 4 * term

    return approx_pi


def get_pi_from_leibniz_series():
    try:
        iterations = int(input("Enter the number of iterations for pi calculation: "))
        precision = int(input("Enter the number of decimal places for precision: "))
        if iterations <= 0 or precision <= 0:
            print("Please enter a positive integer.")
        else:
            pi_approximation = calculate_pi_series(iterations, precision)
            print("Approximation of pi:", pi_approximation)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")