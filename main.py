import time
import src.leibniz


def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("logs/test1.log", "a") as file:
        file.write(f"{timestamp}: {message}\n")


def seek(command):
    iterations = 10**8
    pi_estimation = 0
    num_threads = 2

    pi_calc = src.leibniz.LeibnizPi(iterations)

    delta = time.time()
    pi_estimation = pi_calc.calculate_pi(num_threads)
    print(pi_estimation, time.time() - delta)


def main():
    while True:
        command = input("piSeeker> ")

        command = command.split()

        if command == "exit":
            exit()

        elif command[0] == "seek":
            seek(command)

        else:
            print("Error: command not found!")


if __name__ == "__main__":
    main()