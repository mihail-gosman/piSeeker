import math

def calculate_pi_archimedes(iterations):
    sides = 6
    side_length = 1
    for _ in range(iterations):
        sides *= 2
        side_length = math.sqrt(2 - math.sqrt(4 - side_length**2))

        print(side_length)
    return sides * side_length / 2