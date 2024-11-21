import numpy as np
import time
import threading

# Matrix multiplication with larger matrices to stress CPU and memory
def matrix_multiplication_task():
    size = 2000  # Increased matrix size to 2000x2000
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    while True:
        np.dot(A, B)  # Matrix multiplication (dot product)

# Inefficient recursive Fibonacci calculation with a larger number
def fibonacci_task(n):
    if n <= 1:
        return n
    else:
        return fibonacci_task(n-1) + fibonacci_task(n-2)

def fibonacci_stress():
    while True:
        fibonacci_task(40)  # Calculate Fibonacci of 40 (much more CPU-intensive)

# Prime number generator (inefficient, checking for primes using brute force)
def prime_number_task(limit):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def prime_stress():
    while True:
        prime_number_task(100000)  # Find primes up to 100,000 (CPU-intensive)

# Memory stress task to consume RAM
def memory_stress():
    while True:
        _ = np.random.rand(10000, 10000)  # Create large random matrices, consuming memory

# Function to run a stress test using multiple threads
def cpu_stress_test():
    threads = []
    
    # Launch multiple threads to keep the CPU busy
    for _ in range(8):  # Create 8 threads for each task to maximize CPU usage
        t1 = threading.Thread(target=matrix_multiplication_task)
        t2 = threading.Thread(target=fibonacci_stress)
        t3 = threading.Thread(target=prime_stress)
        t4 = threading.Thread(target=memory_stress)
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        threads.append(t4)
        t1.start()
        t2.start()
        t3.start()
        t4.start()

    # Run for a specific duration (for example, 120 seconds)
    time.sleep(120)  # Run the stress test for 120 seconds

    # Stop the threads after the time is up
    for t in threads:
        t.join()

# Main function to initiate the test
if __name__ == "__main__":
    print("Starting enhanced CPU stress test...")
    cpu_stress_test()
    print("CPU stress test completed.")
