"""
Problem 20: https://projecteuler.net/problem=20
Factorial digit sum
"""

from math import factorial as f
n = int(input("Enter the factorial(without !)"))
print ("Sum of digits for %d! is %d" % (n, sum(map(int, str(f(n))))))
