import numpy



def calc(iterations):
    for i in range(iterations):


try:
    iterations = int(input("Enter the number of iterations for pi calculation: "))
    if iterations <= 0:
        print("Please enter a positive integer.")
    else:
        calc(iterations)
except ValueError:
    print("Invalid input. Please enter a valid integer.")