import argparse


def print_hello_message():
    print("""
-----------------------------------------------------------
  Welcome to piSeeker - version: 0.1  
  Type 'help' for options, 'exit' to quit.
-----------------------------------------------------------
    """)


def exit_command(args):
    print("Thank you for using piSeeker. Goodbye!")
    exit()


COMMANDS = {
    'exit': exit_command
}


def handle_command(user_input):
    command = user_input[0]
    args = user_input[1:]

    if command in COMMANDS:
        COMMANDS[command](args)


def main():
    print_hello_message()

    while True:
        user_input = input("piSeeker> ").strip().lower().split()
        handle_command(user_input)


if __name__ == "__main__":
    main()
