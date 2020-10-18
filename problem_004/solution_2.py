"""
Question 4: https://projecteuler.net/problem=4

  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
  Find the largest palindrome made from the product of two 3-digit numbers.

  Solution 1:
    1. Brute force. Multiply all 3 digit numbers and and check for biggest pallindrome
"""

def isPalindrome(number):
    itoa = str(number)
    first = 0
    last = len(itoa)-1

    while first < last:
        if itoa[first] != itoa[last]:
            return False
        first += 1
        last -= 1
    return True

def findPalindrome():
    biggestPalindrome = 0
    factor = [0,0]
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            if isPalindrome(i*j) and (i*j)> biggestPalindrome:
                biggestPalindrome = i*j
                factor[0] = i
                factor[1] = j
    print("Largest pallindrome with 3 digit factors: {0} X {1} = {2}".format( factor[0] ,factor[1] ,factor[0]*factor[1]))
    return biggestPalindrome


findPalindrome()

