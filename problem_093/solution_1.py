def oper(x,y,op):
    if op==0: return x+y
    elif op==1: return x-y
    elif op==2: return x*y
    else: return x//y

# one expression with concatenated operators
def genexpr(results,l,m,p,o2,o3):
    a = oper(l[p[0]],l[p[0]+1],m[p[0]])
    if o2=='r': b = oper(a,l[p[1]+1],m[p[1]])
    elif o2=='s': b = oper(l[p[1]],l[p[1]+1],m[p[1]])
    else:
        if a==0 and m[p[1]]==3: return
        b = oper(l[p[1]],a,m[p[1]])
    if o3=='r': c = oper(b,l[p[2]+1],m[p[2]])
    elif o3=='s':
        if b==0 and m[p[2]]==3: return
        c = oper(a,b,m[p[2]])
    else:
        if b==0 and m[p[2]]==3: return
        c = oper(l[p[2]],b,m[p[2]])
    if False:
        ops = ['+','-','*','/']
        print(l[0],ops[m[0]],l[1],ops[m[1]],l[2],ops[m[2]],l[3],'=',c,' - ',p,o2,o3,a,b)
    if c>0: results.add(c)

# all combinations of precedence
def genbraces(results,l,m):
    genexpr(results,l,m,[0,1,2],'r','r')
    genexpr(results,l,m,[0,2,1],'s','s')
    genexpr(results,l,m,[1,0,2],'l','r')
    genexpr(results,l,m,[1,2,0],'r','l')
    #genexpr(results,l,m,[2,0,1],'s','s') - duplicate of [0,2,1]
    genexpr(results,l,m,[2,1,0],'l','l')

# all combinations of the 3 operators
def genoperators(results,l):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                genbraces(results,l,[a,b,c])        
               
# all distinct combinations of the 4 numbers in l
def gennumbers(l):
    results=set()
    for a in l:
         for b in [x for x in l if x != a]:
            for c in [x for x in l if x not in [a,b]]:
                for d in [x for x in l if x not in [a,b,c]]:
                    genoperators(results,[a,b,c,d])
    return results;

# all distinct sets of 4 numbers
#gennumbers([1,2,3,4])
maxstreak = 0
for a in range(1,10):
    for b in [x for x in range(1,10) if x > a]:
            for c in [x for x in range(1,10) if x > a and x > b]:
                for d in [x for x in range(1,10) if x > a and x > b and x > c]:
                    results=gennumbers([a,b,c,d])
                    resorder=sorted(list(results))
                    y=1
                    while(y==resorder[y-1]): y+=1
                    y-=1
                    if y>=maxstreak:
                        maxstreak=y                        
                        print(maxstreak,":",a,b,c,d," - ",len(results),max(resorder))
                    
