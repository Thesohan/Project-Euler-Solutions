# Euler 36 : Double-base palindromes
# Link : https://projecteuler.net/problem=36

#sum of all numbers less than 1,000,000 that are palindromic in base 10 and base 2

total = 0
for num in range(1,1000001,2):

	if str(num) == str(num)[::-1]:
		x = bin(num).replace("0b","")
		if str(x) == str(x)[::-1]:
			total = total + num

print(total)