import Primes
maxn=1000001
ch=[]
for i in range(maxn):
    ch.append(False)
pr=Primes.properfacs(maxn)
maxc=0
mine=0
for i in range(1,maxn):
    if ch[i]:
        continue
    j=sum(pr[i])
    amic=[i]
    while j!=i: 
        if j>1000000 or j<=1:
            amic=[]
            break
        if j in amic:
            ind=amic.index(j)
            amic=amic[ind:]
            break
        ch[j]=True
        amic.append(j)
        j=sum(pr[j])
    if len(amic)>maxc:
        maxc=len(amic)
        mine=j
        print(mine,maxc)
        