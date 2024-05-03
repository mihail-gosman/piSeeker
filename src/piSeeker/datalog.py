import os


class DataLogger:
    def __init__(self, directory="logs"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)
        self.log_filename = self.get_next_log_filename()

    def get_next_log_filename(self):
        files = os.listdir(self.directory)
        log_files = [f for f in files if f.endswith('.txt')]
        num_log_files = len(log_files)
        return os.path.join(self.directory, f"test_log_{num_log_files + 1}.txt")

    def log_data(self, data_list):
        with open(self.log_filename, 'a') as txtfile:
            for data in data_list:
                txtfile.write(f"{data}\n")
