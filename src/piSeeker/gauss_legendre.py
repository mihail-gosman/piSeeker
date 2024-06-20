def calculate_pi_gauss_legendre(iterations):
    a, b, t, p = 1.0, 1.0 / 2**0.5, 0.25, 1.0
    for _ in range(iterations):
        a_n = (a + b) / 2
        b = (a * b)**0.5
        t -= p * (a - a_n)**2
        a = a_n
        p *= 2
    return (a + b)**2 / (4 * t)