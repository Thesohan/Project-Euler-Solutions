# Euler 47: Distinct Prime Factors
# Link : https://projecteuler.net/problem=47

#find the first four consecutive integers that each have four distinct prime factors (return first of these numbers)
import math
maximum = 1000000 #set a bound on the search
sol = 0
def num_prime_factors(n):
    factors = set()
    i = 2 #to exclude 1
    while i <= int(math.sqrt(n)):
    	if n % i:
    		i = i + 1
    	else:
    		n //= i
    		factors.add(i)
    if n > 1:
    	factors.add(n)
    return len(factors)

for i in range(1,maximum):
	if num_prime_factors(i) == 4:
		if num_prime_factors(i+1) == 4:
			if num_prime_factors(i+2) == 4:
				if num_prime_factors(i+3) == 4:
					sol = i
					break

print(sol)
