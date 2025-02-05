import time
import matplotlib.pyplot as plt


def primelist1(n):
    if n < 2:
        return
    print(2)
    for j in range(3, n):
        isprime = True
        for i in range(2, j-1):
            if j % i == 0:
                isprime = False
        if isprime:
            print(j)

def primelist2(n):
    if n < 2:
        return
    print(2)
    for j in range(3, n):
        isprime = True
        for i in range(2, int(j**0.5)):
            if j % i == 0:
                isprime = False
        if isprime:
            print(j)

def primelist3(n):
    if n < 2:
        return
    print(2)
    for j in range(3, n):
        isprime = True
        for i in range(2, int(j**0.5)):
            if j % i == 0:
                isprime = False
                break
        if isprime:
            print(j)

n_values = [1000, 2000, 5000, 10000, 20000, 50000]

timingData1 = []
timingData2 = []
timingData3 = []

num_trials = 5

for n in n_values:
    total_time_1 = 0.0
    total_time_2 = 0.0
    total_time_3 = 0.0
    
    for _ in range(num_trials):
        start = time.time()
        primelist1(n)
        end = time.time()
        total_time_1 += (end - start)
        
        start = time.time()
        primelist2(n)
        end = time.time()
        total_time_2 += (end - start)
        
        start = time.time()
        primelist3(n)
        end = time.time()
        total_time_3 += (end - start)
    
    avg_time_1 = total_time_1 / num_trials
    avg_time_2 = total_time_2 / num_trials
    avg_time_3 = total_time_3 / num_trials
    
    timingData1.append(avg_time_1)
    timingData2.append(avg_time_2)
    timingData3.append(avg_time_3)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0,0].scatter(n_values, timingData1, color='red', marker='o')
axs[0,0].set_title('primelist1')
axs[0,0].set_xlabel('n')
axs[0,0].set_ylabel('Average T (s)')
axs[0,0].grid(True)

axs[0,1].scatter(n_values, timingData2, color='blue', marker='s')
axs[0,1].set_title('primelist2')
axs[0,1].set_xlabel('n')
axs[0,1].set_ylabel('Average T(n) (s)')
axs[0,1].grid(True)

axs[1,0].scatter(n_values, timingData3, color='green', marker='^')
axs[1,0].set_title('primelist3')
axs[1,0].set_xlabel('n')
axs[1,0].set_ylabel('Average T(n) (s)')
axs[1,0].grid(True)

axs[1,1].scatter(n_values, timingData1, color='red', marker='o', label='primelist1')
axs[1,1].scatter(n_values, timingData2, color='blue', marker='s', label='primelist2')
axs[1,1].scatter(n_values, timingData3, color='green', marker='^', label='primelist3')
axs[1,1].set_title('All Primelist Averages')
axs[1,1].set_xlabel('n')
axs[1,1].set_ylabel('Average T(n) (s)')
axs[1,1].legend()
axs[1,1].grid(True)

plt.tight_layout()
plt.show()
