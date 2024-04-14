import numpy as np
import time
import multiprocessing
import matplotlib.pyplot as plt
import pandas as pd
import psutil

def generate_random_matrix(size):
    return np.random.rand(size, size)

def multiply_matrices(constant_matrix, num_matrices):
    results = []
    for _ in range(num_matrices):
        random_matrix = generate_random_matrix(constant_matrix.shape[0])
        result_matrix = np.matmul(random_matrix, constant_matrix)
        results.append(result_matrix)
    return results

def multiply_matrices_parallel(constant_matrix, num_matrices, num_threads):
    pool = multiprocessing.Pool(processes=num_threads)
    results = pool.starmap(multiply_matrices, [(constant_matrix, num_matrices//num_threads)] * num_threads)
    pool.close()
    pool.join()
    return results

def get_cpu_usage():
    return psutil.cpu_percent(percpu=True)

if __name__ == "__main__":
    matrix_size = 1000
    constant_matrix = generate_random_matrix(matrix_size)
    num_matrices = 100
    num_threads = [1, 2, 3, 4, 5, 6, 7, 8]
    time_taken = []

    cpu_usage = []

    for t in num_threads:
        start_time = time.time()
        _ = multiply_matrices_parallel(constant_matrix, num_matrices, t)
        end_time = time.time()
        time_taken.append(end_time - start_time)
        
        cpu_usage.append(get_cpu_usage())

    # Plotting Thread vs. Time
    plt.figure(figsize=(10, 5))
    plt.plot(num_threads, time_taken, marker='o')
    plt.title('Time Taken vs. Threads')
    plt.xlabel('Threads')
    plt.ylabel('Time Taken (seconds)')
    plt.grid(True)
    plt.show()

    # Plotting CPU Usage of Different Cores
    cpu_usage = np.array(cpu_usage)
    num_cores = cpu_usage.shape[1]
    plt.figure(figsize=(10, 5))
    for core in range(num_cores):
        plt.plot(num_threads, cpu_usage[:, core], marker='o', label=f'CPU {core+1}')
    plt.title('CPU Usage of Different Cores vs. Threads')
    plt.xlabel('Threads')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Creating DataFrame for table
    df = pd.DataFrame({'Threads': num_threads, 'Time Taken (Sec)': time_taken})
    print(df)