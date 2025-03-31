import time
from tabulate import tabulate

def largestFib(k):
    if k <= 2:
        return 0, 0
    a, b = 1, 1
    count = 2
    while b < k:
        a, b = b, a + b
        count += 1
    return a, count - 1

def time_fib(val):
    start = time.perf_counter()
    fib_val, fib_count = largestFib(val)
    end = time.perf_counter()
    total_time = end - start
    return fib_val, fib_count, total_time

print("")
fib_val_1, fib_count_1, total_time_1 = time_fib(2**4)
print(f"F({fib_count_1}) = {fib_val_1} < 2^4")
fib_val_2, fib_count_2, total_time_2 = time_fib(2**8)
print(f"F({fib_count_2}) = {fib_val_2} < 2^8")
fib_val_3, fib_count_3, total_time_3 = time_fib(2**16)
print(f"F({fib_count_3}) = {fib_val_3} < 2^16")
fib_val_4, fib_count_4, total_time_4 = time_fib(2**32)
print(f"F({fib_count_4}) = {fib_val_4} < 2^32")
fib_val_5, fib_count_5, total_time_5 = time_fib(2**64)
print(f"F({fib_count_5}) = {fib_val_5} < 2^64")

print("")
data1 = [
    ["Nibble",                4,  fib_val_1,  total_time_1],
    ["Byte",                  8,  fib_val_2, total_time_2],
    ["Unsigned short int",   16, fib_val_3, total_time_3],
    ["Unsigned int",         32, fib_val_4, total_time_4],
    ["Unsigned long",        64, fib_val_5, total_time_5],
]
header1 = ["Data Type", "n bits", "F(n)", "Computation Time"]
print(tabulate(data1, headers=header1, tablefmt="grid"))

def time_fib_avg(val, runs=100000):
    start = time.perf_counter()
    fib_val = fib_count = 0
    for _ in range(runs):
        fib_val, fib_count = largestFib(val)
    end = time.perf_counter()
    total_time = end - start
    avg_time = total_time / runs
    return fib_val, fib_count, total_time, avg_time

fib_val_1, fib_count_1, total_run_time_1, avg_time_1 = time_fib_avg(2**4, 100000)
fib_val_2, fib_count_2, total_run_time_2, avg_time_2 = time_fib_avg(2**8, 100000)
fib_val_3, fib_count_3, total_run_time_3, avg_time_3 = time_fib_avg(2**16, 100000)
fib_val_4, fib_count_4, total_run_time_4, avg_time_4 = time_fib_avg(2**32, 100000)
fib_val_5, fib_count_5, total_run_time_5, avg_time_5 = time_fib_avg(2**64, 100000)

print("")
data2 = [
    ["Nibble",                4,  fib_val_1,  total_run_time_1, avg_time_1],
    ["Byte",                  8,  fib_val_2, total_run_time_2, avg_time_2],
    ["Unsigned short int",   16, fib_val_3, total_run_time_3, avg_time_3],
    ["Unsigned int",         32, fib_val_4, total_run_time_4, avg_time_4],
    ["Unsigned long",        64, fib_val_5, total_run_time_5, avg_time_5],
]
header2 = ["Data Type", "n bits", "F(n)", "Total time (100000 runs)", "Avg time per run"]
print(tabulate(data2, headers=header2, tablefmt="grid"))

