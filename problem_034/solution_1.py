## Problem 34 - Digit Factorials
## https://projecteuler.net/problem=34
## Author: andreibogdanflorea

import math


def compute():
  # A number bigger than 10^n for n >= 8 cannot be equal to the sum of the 
  # factorial of its digits, because 9! * n < 10 ^ n
	ans = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
	return str(ans)


def factorial_digit_sum(n):
	crt_sum = 0
	while n > 0:
		crt_sum += factorials[n % 10]
		n //= 10
	return crt_sum


factorials = list(math.factorial(x) for x in range(10))
print(factorials)
print(compute())
