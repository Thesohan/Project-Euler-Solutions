"""
Problem 48: https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.



We are only interested in the last 10 digits so we can use mod 10 000 000 000 to cut off the first digits and avoid storing them in memory

modulo also has these useful properties:

(A * B) mod C = ((A mod C) * (B mod C)) mod C
(A + B) mod C = ((A mod C) + (B mod C)) mod C
"""

def getLastDigits(numberOfDigits: int):
    bigModulo = 10 ** numberOfDigits

    result = 0
    for currentNumber in range(1, 1001):
        temp = currentNumber
        for i in range(1, currentNumber):
            temp *= (currentNumber % bigModulo) # this mod operation is redundant but helps demonstrate the function (A * B) mod C
            temp %= bigModulo
        
        result += (temp % bigModulo) # this mod operation is redundant but helps demonstrate the function (A + B) mod C
        result %= bigModulo
    
    return result

print("The last " + str(10) + " digits are: " + str(getLastDigits(10)))