hits=1  # amount found
sumn=16 # (5,5,6)
prev=2  # (1,1,0)
curr=8  # 4*prev-0
while True:
    temp=curr
    curr=4*curr-prev
    prev=temp
    if (hits&1)==1:
        a=(-2+(4+12*(curr**2+1))**0.5)/6 # solves 3a^2+2a-1
        per=3*a-1
    else:
        a=(2+(4+12*(curr**2+1))**0.5)/6  # solves 3a^2-2a-1
        per=3*a+1
    if per>10**9: break
    sumn+=per
    hits+=1
print(int(sumn))



