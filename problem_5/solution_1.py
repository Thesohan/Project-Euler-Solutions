#Problem 5
#https://projecteuler.net/problem=5
def hcf(x,y): return y and hcf(y, x % y) or x
def lcm(x,y): return x * y / hcf(x,y)
def solution():
    n = 1
    for i in range(1, 31):
        n = lcm(n, i)
    print(n)
solution()
