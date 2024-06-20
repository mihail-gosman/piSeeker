def calculate_pi_nilakantha(iterations):
    pi = 3.0
    sign = 1
    for i in range(2, 2 + 2 * iterations, 2):
        pi += sign * 4 / (i * (i + 1) * (i + 2))
        sign *= -1
    return pi