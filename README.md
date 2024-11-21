CPU Stress Test Script

This Python script is made for stress-testing your CPU and memory by running multiple resource-intensive tasks in parallel. 
The tasks include:

    1. Matrix Multiplication with large matrices.
    2. Recursive Fibonacci Calculation for a larger Fibonacci number.
    3. Prime Number Calculation using an inefficient brute-force method.
    4. Memory Stress by generating large random matrices.

It uses multithreading to maximize CPU usage and numpy for matrix operations.

Requirements:

    Python 3.x
    numpy library

Setup Instructions:

(Virtual Environment is always recommended to run python scripts).

Follow these steps to set up and run the script in a virtual environment.

1. Install Python (if not already installed)

Make sure you have Python 3.x installed on your machine. You can download Python from the official Python website.

To verify if Python is already installed, run the following command:

python --version

If it is not installed, download and install Python from the official python website: https://www.python.org/

2. Create a Virtual Environment (optional but recommended)

Using a virtual environment helps isolate project dependencies from your system-wide Python installation.
Install virtualenv (if not installed):

pip install virtualenv

Create a Virtual Environment:

Navigate to the folder where you want to store the project and create a virtual environment:

virtualenv venv

Activate the Virtual Environment:

    Windows:

.\venv\Scripts\activate

Linux/macOS:

    source venv/bin/activate

Once activated, your terminal prompt should display (venv) indicating that you're working inside the virtual environment.

3. Install Dependencies

With the virtual environment activated, install the required Python package numpy by running:

pip install numpy

4. Download the Script

Save the provided Python script (e.g., cpu_stress_test.py) to your desired directory.
5. Run the Script

To start the CPU stress test, execute the following command:

python cpu_stress_test.py

The script will run for 120 seconds, utilizing CPU and memory resources through multithreading. During this time, you can monitor the system’s resource usage (CPU and RAM) to observe the stress test.

6. Deactivate the Virtual Environment (Optional)

Once you're done with the stress test, you can deactivate the virtual environment:

deactivate

This will return you to your system’s default Python environment.
How the Script Works

    1. Matrix Multiplication: The script generates two large 2000x2000 matrices and performs continuous matrix multiplication, which consumes significant CPU resources.
    2. Fibonacci Calculation: The script recursively calculates the 40th Fibonacci number, which is highly inefficient and CPU-intensive.
    3. Prime Number Calculation: The script checks for prime numbers up to 100,000 using brute-force trial division, which is computationally expensive.
    4. Memory Stress: The script generates large random matrices (10000x10000), which will consume a large amount of system memory.

Monitoring the System During the Test

You can monitor your system's resource usage during the stress test:

    CPU Usage:
        On Linux/macOS, use the top or htop or btop commands.
        On Windows, open Task Manager (Ctrl+Shift+Esc) and check the Performance tab.
    Memory Usage: Monitor memory usage in the same way through Task Manager (Windows) or free/top (Linux/macOS).

Notes

    Warning: This script is highly resource-intensive and can make your system slow or unresponsive, especially if you're running it on a machine with limited resources. It’s best to run it on a test machine or a system where performance degradation is acceptable.

    Duration: The script runs for 120 seconds by default. You can modify the time.sleep(120) value in the script if you want to adjust the duration.

License

This script is released under the MIT License. Feel free to use, modify, and distribute it as needed.
