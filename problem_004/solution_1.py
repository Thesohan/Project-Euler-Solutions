"""
Largest palindrome product
Problem 4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False
isFound=False
for i in range(999,100,-1):
    if isFound:
        break
    for j in range(999,100,-1):
        if isPalindrome(i*j):
            print(i*j)
            isFound=True
            break
            
