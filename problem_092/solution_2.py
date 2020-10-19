def sd(n):
    sumd=0;
    while n>0:
        sumd+=(n%10)**2;
        n=int(n/10);
    return sumd;

maxn=10000000;
c89=0;
for i in range(1,maxn):
    j = i;
    while j != 1 and j != 89:
        j = sd(j);
    if j == 89:
        c89+=1;
print(c89);        
