import src.leibniz


def seek():



def main():
    while True:
        command = input("piSeeker> ")

        command = command.split()

        if command == "exit":
            exit()

        elif command[0] == "seek":
            seek()

        else:
            print("Error: command not found!")


if __name__ == "__main__":
    main()