import time

def primeTest(x, start_time, time_limit):
    if x < 2:
        return False
    for k in range(2, int(x**0.5) + 1):
        if k % 100 == 0:
            if (time.time() - start_time) >= time_limit:
                print("3 hours reached")
                return 
        if x % k == 0:
            return False
    return True

def LucasLehmer(p):
    if p == 2:
        return True
    s = 4
    m = (1 << p) - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    return (s == 0)

def function_i():
    print("----------------------------------------------------------------")
    start_time = time.time()
    found = 0
    n = 2
    time_limit = 10800 
    max_perfects = 20

    while found < max_perfects:
        if (time.time() - start_time) >= time_limit:
            print("3 hours reached")
            return
        
        if n > 1:
            total_div = 1
            for d in range(2, int(n**0.5) + 1):
                if (time.time() - start_time) >= time_limit:
                    print("3 hours reached")
                    return
                if n % d == 0:
                    total_div += d
                    other = n // d
                    if other != d:
                        total_div += other

            if total_div == n:
                print(n)
                print()
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached. Elapsed time:",
                          time.time() - start_time)
                    return
        n += 1

    if found == max_perfects:
        print("20 perfect numbers reached. Elapsed time:",
              time.time() - start_time)

def function_ii():
    print("----------------------------------------------------------------")
    start_time = time.time()
    found = 0
    p = 2
    time_limit = 10800 
    max_perfects = 20

    while found < max_perfects:
        if (time.time() - start_time) >= time_limit:
            print("3 hours reached")
            return

        if primeTest(p, start_time, time_limit):
            if (time.time() - start_time) >= time_limit:
                print("3 hours reached")
                return

            m = (1 << p) - 1
            if primeTest(m, start_time, time_limit):
                if (time.time() - start_time) >= time_limit:
                    print("3 hours reached")
                    return

                print(p)
                print((1 << (p - 1)) * m)
                print()
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached. Elapsed time:",
                          time.time() - start_time)
                    return
        p += 1

    if found == max_perfects:
        print("20 perfect numbers reached. Elapsed time:",
              time.time() - start_time)

def function_iii():
    print("----------------------------------------------------------------")
    start_time = time.time()
    found = 0
    p = 2
    time_limit = 10800
    max_perfects = 20

    while found < max_perfects:
        if (time.time() - start_time) >= time_limit:
            print("3 hours reached")
            return

        if primeTest(p, start_time, time_limit):
            if (time.time() - start_time) >= time_limit:
                print("3 hours reached")
                return

            m = (1 << p) - 1
            if LucasLehmer(p):
                if (time.time() - start_time) >= time_limit:
                    print("3 hours reached")
                    return

                print(p)
                print((1 << (p - 1)) * m)
                print()
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached. Elapsed time:",
                          time.time() - start_time)
                    return
        p += 1

    if found == max_perfects:
        print("20 perfect numbers reached. Elapsed time:",
              time.time() - start_time)

function_i()
function_ii()
function_iii()


