"""
Problem 7: https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math,time

def is_prime(n):
    if n < 2: 
         return False
    if n % 2 == 0:
        if n==2:
            return True
        return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def get_prime(prime):
    s = time.time()
    count = 0
    for i in range(10000000):
        if is_prime(i):
            count += 1
            if count == prime:
                print(i) # prints prime number
                break
    print(time.time()-s) # prints the execution time

get_prime(10001)