import time
import src.leibniz


def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("logs/test1.log", "a") as file:
        file.write(f"{timestamp}: {message}\n")


def seek(command):
    iterations = 10**11
    step_size = 10**6
    pi_estimation = 0

    log_message(f"Starting benchmark test number: 1, algorithm: leibnitz 0.1, iterations: {iterations}, step_size: {step_size} ")

    start_time = time.time()

    for n in range(step_size, iterations+step_size, step_size):
        delta_time = time.time()
        pi_estimation += src.leibniz.leibniz(n-step_size, n)
        delta_time = time.time() - delta_time

        q = time.time()
        log_message(f"PI estimation: {pi_estimation}, total time: {time.time() - start_time}, step time: {delta_time}, termen: {n}")
        q = time.time() - q
        print(q)

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