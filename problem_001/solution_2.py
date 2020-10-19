"""
Problem 1: https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
from math import ceil


def solution(lim: int = 1000):
    """
    Instead of generating all numbers under the limit and checking if they're divisible by 3/5,
    we generate all numbers that multiplied by either 3 or 5 are under 1000 and add them together.
    In other words, we don't traverse numbers that are unnecessary. 
    (This leads to almost halving the time of execution if lim = 1,000,000)
    """
    return sum([n * 3 for n in range(1, ceil(lim / 3)) if n % 5 != 0]) + sum([n * 5 for n in range(1, ceil(lim / 5))])


if __name__ == "__main__":
    print(solution(int(input("Enter upper limit:	").strip())))
