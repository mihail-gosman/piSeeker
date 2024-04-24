import decimal


def calc(iterations, precision):
    decimal.getcontext().prec = precision
    terms = []
    term = decimal.Decimal()

    for i in range(iterations):
        term = (decimal.Decimal('-1') ** decimal.Decimal(str(i))) / (decimal.Decimal("2") * decimal.Decimal(str(i)) + decimal.Decimal("1"))
        terms.append(term)

    pi = 0
    for i in terms:
        pi += 4 * i



def leibniz_pi():
    try:
        iterations = int(input("Enter the number of iterations for pi calculation: "))
        precision = int(input("Enter the number of decimal places for precision: "))
        if iterations <= 0 or precision <= 0:
            print("Please enter a positive integer.")
        else:
            calc(iterations, precision)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
