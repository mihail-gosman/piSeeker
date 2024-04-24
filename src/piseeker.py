import piSeeker.leibniz_pi


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


def seek_command(arguments):
    algorithms = {
        'leibniz': piSeeker.leibniz_pi.leibniz_pi,
    }

    if arguments and arguments[0] in algorithms:
        algorithms[arguments[0]]()
    else:
        print("Invalid or no algorithm provided.")


def help_command(arguments):
    pass


def main():
    commands = {
        'help': help_command,
        'seek': seek_command,
        'exit': exit_command
    }

    print_hello_message()

    while True:
        user_input = input("piSeeker> ").split()

        command = user_input[0]
        arguments = user_input[1:]

        if command in commands:
            commands[command](arguments)
        else:
            print("Invalid command. Use 'help' for available commands.")


if __name__ == "__main__":
    main()
