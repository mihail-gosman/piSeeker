import time

import numpy as np
import time


def leibniz_pi(num_terms):
    start_time = time.time()

    terms = np.arange(num_terms)
    numerators = (-1) ** terms
    denominators = 2 * terms + 1
    pi_estimate = 4 * np.sum(numerators / denominators)
    end_time = time.time()
    calculation_time = end_time - start_time
    return pi_estimate, calculation_time


def leibniz(iterations):
    partial_sum = 0

    delta = time.time()

    for i in range(iterations):
        partial_sum += ((-1)**i)/(i*2+1)

    delta = time.time() - delta

    partial_sum *= 4

    return partial_sum, delta

