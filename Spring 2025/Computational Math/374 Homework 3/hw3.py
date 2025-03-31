import time

def primeTest(x):
    if x < 2:
        return False
    for k in range(2, int(x**0.5) + 1):
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
                if n % d == 0:
                    total_div += d
                    other = n // d
                    if other != d:
                        total_div += other
            if total_div == n:
                print(n)
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached")
                    return
        n += 1

    if found == max_perfects:
        print("20 perfect numbers reached")

def function_ii():
    start_time = time.time()
    found = 0
    p = 2
    time_limit = 10800
    max_perfects = 20

    while found < max_perfects:
        if (time.time() - start_time) >= time_limit:
            print("3 hours reached")
            return
        if primeTest(p):
            m = (1 << p) - 1
            if primeTest(m):
                print(p, (1 << (p - 1)) * m)
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached")
                    return
        p += 1

    if found == max_perfects:
        print("20 perfect numbers reached")

def function_iii():
    start_time = time.time()
    found = 0
    p = 2
    time_limit = 10800
    max_perfects = 20

    while found < max_perfects:
        if (time.time() - start_time) >= time_limit:
            print("3 hours reached")
            return
        if primeTest(p):
            m = (1 << p) - 1
            if LucasLehmer(p):
                print(p, (1 << (p - 1)) * m)
                found += 1
                if found == max_perfects:
                    print("20 perfect numbers reached")
                    return
        p += 1

    if found == max_perfects:
        print("20 perfect numbers reached")

function_i()