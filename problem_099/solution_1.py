import math
file=open('p099_base_exp.txt','r')
line=0;maxline=0
m=0;n=0
for f in file.readlines():
    line+=1
    pair = f.split(',')
    a = int(pair[0]);b = int(pair[1])
    if m==0:
        m=a;n=b
    elif m>a:
        x=math.log(m/a)/math.log(a)
        if x*n<(b-n):
            m=a;n=b
            maxline=line
    else:
        x=math.log(a/m)/math.log(m)
        if x*b>(n-b):
            m=a;n=b
            maxline=line
print(m,n);print(maxline)    
