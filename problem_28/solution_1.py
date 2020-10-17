"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# Incidentally, the closed form of this sum is (4m^3 + 3m^2 + 8m - 9) / 6, where m = size.


def compute():
    SIZE = 1001  # Must be odd
    ans = 1  # Special case for size 1
    ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, SIZE + 1, 2))
    return str(ans)


if __name__ == "__main__":
    print(compute())
