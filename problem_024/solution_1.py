"""
Problem 24: https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solution based on https://en.wikipedia.org/wiki/Factorial_number_system
"""
from math import floor, factorial


def solution(digits: list, position: int):
    result = []  # To populate intermediate numbers
    remainder = position - 1
    # Only use factorial function once as afterwards we can just divide by the last number
    fact = factorial(len(digits) - 1)
    # Iterate in reverse order for the permutations at each position, i.e. 9! to 0! in default case
    for i in range(len(digits) - 1, -1, -1):
        pos = floor(remainder / fact)
        digit = digits[pos]
        result.append(digit)
        remainder = remainder % fact
        digits.remove(digit)
        if i != 0:
            fact /= i
    return result


if __name__ == "__main__":
    print(*solution(list(range(10)), 1000000))
