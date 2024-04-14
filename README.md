# UCS654 Assignment-7
Multiply 100 random matrices of size 1k x 1k with a constant matrix of size 1k x 1k and generate the result table, graph and CPU usages.

## Methodology:-

### Objective:
The objective of this code is to benchmark the performance of matrix multiplication across different numbers of threads using multiprocessing. Additionally, it monitors CPU usage across different cores during the matrix multiplication process.

### Methodology:

Matrix Multiplication:

The code generates a random square matrix of a specified size using NumPy.
It defines functions to perform matrix multiplication:
generate_random_matrix(size): Generates a random square matrix of the specified size.
multiply_matrices(constant_matrix, num_matrices): Multiplies a constant matrix by a specified number of random matrices.
multiply_matrices_parallel(constant_matrix, num_matrices, num_threads): Utilizes multiprocessing to perform matrix multiplication in parallel using a specified number of threads.

CPU Monitoring:

The code utilizes the psutil library to monitor CPU usage.
The function get_cpu_usage() retrieves CPU usage percentages for each core.

Benchmarking:

The code loops over different numbers of threads and measures the time taken for matrix multiplication using each configuration.
It records the time taken for each configuration and CPU usage for each core.

Visualization:

The code plots the relationship between the number of threads and the time taken for matrix multiplication.
It also plots the CPU usage of different cores against the number of threads used.

### Output:

The code generates a table displaying the number of threads and the corresponding time taken for matrix multiplication.

### Technologies Used:

Python: The core programming language used for implementation.

NumPy: Used for matrix operations and generation of random matrices.

multiprocessing: Utilized for parallel processing of matrix multiplication.

matplotlib: Used for data visualization, specifically for plotting graphs.

psutil: Used for monitoring CPU usage.

### How to Use:

Ensure Python and required libraries (numpy, matplotlib, psutil) are installed.\n
Run the script assign_7_code.py.
Review the generated graphs to analyze the relationship between the number of threads and time taken, as well as CPU usage across different cores.
The script also outputs a table displaying the time taken for matrix multiplication using different numbers of threads.
