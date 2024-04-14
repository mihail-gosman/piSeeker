import time


def leibniz(iterations):
    partial_sum = 0

    delta = time.time()

    for i in range(iterations):
        partial_sum += ((-1)**i)/(i*2+1)

    delta = time.time() - delta

    partial_sum *= 4

    return partial_sum, delta

