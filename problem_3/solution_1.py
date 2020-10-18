"""
Problem 3: https://projecteuler.net/problem=3
What is the largest prime factor of the number 600851475143?

"""
import math

def solution(num):

    number=num
    largest_prime_fact = 1

    print("The Prime Factors of "+str(num)+" are:", end = " ")

    #Check for negative numbers or zero
    if num<=0:
        return

    #Displays the number of 2s as the Prime Factors
    while num%2==0:
        largest_prime_fact = 2
        print(2,end=" ")
        num/=2

    #Displays the other Prime Factors of that number
    for i in range(3, int(math.sqrt(num))+1,2):
        while num%i==0:
            largest_prime_fact = i
            print(i,end=" ")
            num/=i

    #Displays the final Prime Factor
    if num>2:
        largest_prime_fact = int(num)
        print(int(num))

    print("\nThe Largest Prime Factor of "+str(number)+" is: "+str(largest_prime_fact))

solution(600851475143)

