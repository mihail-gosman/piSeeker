import piSeeker.leibniz
import piSeeker.datalog


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
        'leibniz': piSeeker.leibniz.get_pi_from_leibniz_series,
    }

    if arguments and arguments[0] in algorithms:
        result = algorithms[arguments[0]]()

        data_log = piSeeker.datalog.DataLogger()
        data_log.log_data(result)

    else:
        print("Invalid or no algorithm provided.")


def help_command(arguments):
    return None


COMMANDS = {
    'help': help_command,
    'seek': seek_command,
    'exit': exit_command
}

if __name__ == "__main__":
    print_hello_message()

    while True:
        user_input = input("piSeeker> ").split()

        if len(user_input) >= 1:
            command = user_input[0]
            arguments = user_input[1:]
        else:
            continue

        if command in COMMANDS:
            COMMANDS[command](arguments)
        else:
            print("Invalid command. Use 'help' for available commands.")
