"""
Problem 25: https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import math

targetDigits = 1000

previous = 1
current = 1
# we start counting the fibonacci indexes from the second element => term counter is 2
termCounter = 2

# log of 10 gives us the current number of digits in the fibonacci number
while(math.log10(current) < targetDigits):
    termCounter +=1
    temp = previous
    previous = current
    current = temp + previous

print("First Fibonacci term with " + str(targetDigits) + " digits is term: " + str(termCounter))