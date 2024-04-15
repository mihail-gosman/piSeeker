import src.leibniz


def main():
    while True:
        command = input("piSeeker> ")

        if command == "exit":
            exit()

        else:
            print("Error: command not found!")


if __name__ == "__main__":
    main()