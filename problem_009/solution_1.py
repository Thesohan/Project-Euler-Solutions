"""
Problem 9: https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
"""
from math import pow, sqrt, floor


def find_factors(n: int):
    """
    Find and return list of tuples that are the factors of a given number
    """
    factors = []
    for i in range(1, floor(sqrt(n))):
        if n % i == 0:
            factors.append((i, int(n / i)))

    return factors


def find_triplet(target_sum: int, limit: int = 1000):
    """
    Find triplets leading up to a given sum, with a given iteration limit
    Triplets are generated using Dickson's method until we find one that has the required sum: 
    https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
    """
    for r in range(2, limit, 2):
        factors = find_factors(int(pow(r, 2) / 2))

        for s, t in factors:
            x = r + s
            y = r + t
            z = r + s + t
            if x + y + z == target_sum:
                return x, y, z


def solution(target_sum: int):
    a, b, c = find_triplet(target_sum)
    return a * b * c


if __name__ == "__main__":
    print(solution(1000))
