import math
import timeit


def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

if __name__ == '__main__':

    start = timeit.default_timer()

    num = 0
    for i in range(1000000000):
        num += i
    print(num)

    stop = timeit.default_timer()
    
    print(stop - start, 'sec')

# This file is changed.
