# piSeeker

piSeeker is a command-line tool for benchmarking different algorithms used to calculate the mathematical constant pi (π). It provides a convenient platform for evaluating the performance of various pi calculation algorithms in terms of computation time, accuracy, and scalability.

## Features

- **Algorithm Selection:** Choose from a selection of pi calculation algorithms, including Monte Carlo, Gauss-Legendre, and BBP formula.
- **Benchmarking Criteria:** Specify benchmarking criteria such as computation time, accuracy, and scalability.
- **Custom Test Cases:** Define custom test cases to evaluate algorithm performance under different scenarios.
- **Automated Benchmarking:** Automate the process of running benchmarking tests with multiple iterations for robust results.
- **Results Display:** View benchmarking results in a clear and concise format, including computation time and accuracy metrics.
- **Logging and Reporting:** Log benchmarking results to files and generate summary reports for documentation and analysis.
- **Error Handling:** Robust error handling ensures graceful handling of unexpected inputs and errors during algorithm execution.
- **Help and Usage Information:** Access comprehensive help and usage information with the "--help" or "-h" option.
- **Interactive Mode (Optional):** Interactively configure benchmarking settings and explore options.
- **Configuration Files:** Define default settings and test cases using configuration files for streamlined usage.

## Usage

To use piSeeker, simply follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/piSeeker.git
   ```

2. **Navigate to the piSeeker Directory:**
   ```
   cd piSeeker
   ```

3. **Install Dependencies (if needed):**
   ```
   pip install -r requirements.txt
   ```

4. **Run piSeeker:**
   ```
   python main.py --algorithm monte_carlo --iterations 1000 --precision 6
   ```

5. **View Results:**
   Benchmarking results will be displayed in the terminal. You can also find detailed logs in the "logs" directory.

For more information on available commands, options, and usage examples, run:
```
python main.py --help
```

## License

piSeeker is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
