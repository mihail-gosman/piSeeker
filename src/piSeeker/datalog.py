import csv
import datetime
import os


class DataLogger:
    def __init__(self, directory="logs"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def get_next_log_filename(self):
        files = os.listdir(self.directory)
        log_files = [f for f in files if f.endswith('.csv')]
        num_log_files = len(log_files)
        return os.path.join(self.directory, f"test_log_{num_log_files + 1}.csv")

    def log_data(self, data):
        timestamp = datetime.datetime.now()
        log_filename = self.get_next_log_filename()
        with open(log_filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp] + data)
