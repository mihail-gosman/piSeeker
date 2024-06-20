def calculate_pi_bbp(iterations):
    pi = 0
    for k in range(iterations):
        pi += (1 / 16**k) * (
            4 / (8 * k + 1) -
            2 / (8 * k + 4) -
            1 / (8 * k + 5) -
            1 / (8 * k + 6)
        )
    return pi