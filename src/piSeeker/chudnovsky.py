from math import factorial, sqrt

def calculate_pi_chudnovsky(iterations):
    C = 426880 * sqrt(10005)
    M, X, L, K = 1, 1, 13591409, 6
    S = L
    for i in range(1, iterations):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += M * L // X
        K += 12
    return C / S