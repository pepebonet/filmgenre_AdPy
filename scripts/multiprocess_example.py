"""
Showing an example of multiprocessing
"""
import multiprocessing as mp
import time
import math


def compute_factorial(n):
    """
    Compute the factorial of a given number
    """
    return math.factorial(n)


if __name__ == '__main__':
    # Your multiprocessing code here

    # List of numbers
    numbers = [50000 + x for x in range(100)]

    # With multiprocessing
    start_time = time.time()
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = pool.map(compute_factorial, numbers)
    end_time = time.time()
    print(f"Time with multiprocessing: {round(end_time - start_time, 2)} seconds")

    # Without multiprocessing
    start_time = time.time()
    results = [compute_factorial(n) for n in numbers]
    end_time = time.time()
    print(f"Time without multiprocessing: {round(end_time - start_time, 2)} seconds")
