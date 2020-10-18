"""
Question 4: https://projecteuler.net/problem=4

  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
  Find the largest palindrome made from the product of two 3-digit numbers.

  Solution 1:
    1. Generate pallindromic strings in reverse order
    2. See if the factors are 3-digit numbers each
"""

def createPalindrome(firstHalf):
    # create palindromic strings from one half of the number
    palin  = firstHalf = str(firstHalf)
    for i in range(len(str(firstHalf))-1, -1, -1):
        palin += firstHalf[i]

    return int(palin)
    

def findLargestPalindrome():
    # 999*999 = 998001. All 3 digit products will be less than this number
    firstHalf = 998

    found = False
    # iterate over palindromic sequences
    while not found:
        #generate pallindrome
        palin = createPalindrome(firstHalf)
        #check if factors are 3digit each
        for i in range(999, 99, -1):
            if i*i < palin:
                # factors greater than sqroot have their corresponding multipliers less than the sqroot of the number. 
                # So don't need to check
                break
            if palin % i == 0:
                if 99  < palin/i and palin/i < 999:
                    print("Largest pallindrome with 3 digit factors: {0} X {1} = {2}".format(i,palin/i,palin))
                    return palin
        firstHalf -=1

findLargestPalindrome()
