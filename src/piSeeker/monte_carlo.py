import random

def calculate_pi_monte_carlo(iterations):
    inside_circle = 0
    for _ in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / iterations