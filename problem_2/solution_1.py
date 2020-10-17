"""
Problem 2: https://projecteuler.net/problem=2
"""

f = [1, 1]

while f[-1] < 4000000:
	if (f[-2] + f[-1]) % 2 == 0:
		f.append(f[-2] + f[-1])

print(sum(f) - 2)
