def calculate_pi_leibniz(iterations):
    pi = 0
    for i in range(iterations):
        pi += (-1)**i / (2 * i + 1)
    return 4 * pi