from piSeeker.leibniz import calculate_pi_leibniz
from piSeeker.archimedes import calculate_pi_archimedes
from piSeeker.monte_carlo import calculate_pi_monte_carlo
from piSeeker.gauss_legendre import calculate_pi_gauss_legendre
from piSeeker.bbp import calculate_pi_bbp
from piSeeker.chudnovsky import calculate_pi_chudnovsky
from piSeeker.nilakantha import calculate_pi_nilakantha


def print_hello_message():
    print("""
-----------------------------------------------------------
  Welcome to piSeeker - version: 0.1  
  Type 'help' for options, 'exit' to quit.
-----------------------------------------------------------
    """)


def exit_command(arguments):
    confirm_exit = input("Are you sure you want to exit the program? (yes/no): ").lower()
    if confirm_exit == 'yes':
        print("Exiting the program.")
        exit()
    else:
        print("Resuming program.")


if __name__ == "__main__":
    print_hello_message()
    i = 9
    print(calculate_pi_bbp(i))
    print(calculate_pi_archimedes(i))
    print(calculate_pi_nilakantha(i))
    print(calculate_pi_gauss_legendre(i))
    print(calculate_pi_chudnovsky(i))
    print(calculate_pi_monte_carlo(i))
    print(calculate_pi_leibniz(i))
