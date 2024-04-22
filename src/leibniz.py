import multiprocessing


class LeibnizPi:
    def __init__(self, num_terms):
        self.num_terms = num_terms
        self.partial_sum = multiprocessing.Value('d', 0)  # Using multiprocessing.Value for shared variable

    def calculate_partial_sum(self, start, end):
        partial_sum = 0
        for i in range(start, end):
            partial_sum += ((-1) ** i) / (2 * i + 1)

        with self.partial_sum.get_lock():
            self.partial_sum.value += partial_sum

    def calculate_pi(self, num_processes):
        terms_per_process = self.num_terms // num_processes
        processes = []
        for i in range(num_processes):
            start = i * terms_per_process
            end = (i + 1) * terms_per_process if i < num_processes - 1 else self.num_terms
            process = multiprocessing.Process(target=self.calculate_partial_sum, args=(start, end))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        pi = 4 * self.partial_sum.value
        return pi