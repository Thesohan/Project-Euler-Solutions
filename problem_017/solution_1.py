"""
Problem 17: https://projecteuler.net/problem=17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import re
base = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

doubles = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

hundreds = "hundred"


def build_written(n: int):
    """
    Form numbers from 1- 20; 20 - 100; 100 - 1000 separately
    Some recursion used in the hundreds
    """
    if n < 20:
        return base[n]
    elif 20 <= n < 100:
        first = n // 10
        remainder = n % 10
        if remainder == 0:
            return doubles[first]
        else:
            return "{}-{}".format(doubles[first], base[remainder])
    elif 100 <= n < 1000:
        remainder = n % 100
        first = n // 100
        if remainder == 0:
            return "{} {}".format(base[first], hundreds)
        else:
            return "{} {} and {}".format(base[first], hundreds, build_written(remainder))
    elif n == 1000:
        return "one thousand"


def count_letters(wordform: str):
    """
    Use regex to get the count of all lowercase characters
    """
    return len(re.findall('[a-z]', wordform))


def solution(limit: int):
    count = 0
    for number in range(1, limit + 1):
        wordform = build_written(number)
        count += count_letters(wordform)
    return count


if __name__ == "__main__":
    print(solution(1000))
