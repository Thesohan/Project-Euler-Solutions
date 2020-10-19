def anagram():
    file=open("p098_words.txt")
    words=file.read().split(",")
    keys=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    gram=dict()
    for w in words:
        key=1
        for c in w:
            if c=='"':
                continue
            key*=keys[ord(c)-ord('A')]
        if key in gram:
            gram[key].append(w)
        else:
            gram[key]=[w]
    for k in gram.keys():
        if len(gram[k])>1:
            print(len(gram[k][0])-2, gram[k])

def check(n):
    if (n**0.5).is_integer():
        print(n)
        return True
    return False
        
def chk_introduce():        
    for a in range(1,10):
        for b in range(10):
            if b==a: continue
            for c in range(10):
                if c in [a,b]: continue
                for d in range(1,10):
                    if d in [a,b,c]: continue
                    for e in range(10):
                        if e in [a,b,c,d]: continue
                        for f in range(10):
                            if f in [a,b,c,d,e]: continue
                            for g in range(10):
                                if g in [a,b,c,d,e,f]: continue
                                for h in range(10):
                                    if h in [a,b,c,d,e,f,g]: continue
                                    for i in range(10):
                                        if i in [a,b,c,d,e,f,g,h]: continue
                                        if check(int(str(a)+str(b)+str(c)+str(d)+str(e)
                                                  +str(f)+str(g)+str(h)+str(i))):
                                            if check(int(str(d)+str(i)+str(f)+str(g)+str(h)
                                                         +str(c)+str(a)+str(e)+str(b))):
                                                print("HOORAY!!!")
        
def chk_creation():
    for a in range(1,10):
        for b in range(1,10):
            if b==a: continue
            for c in range(10):
                if c in [a,b]: continue
                for d in range(10):
                    if d in [a,b,c]: continue
                    for e in range(10):
                        if e in [a,b,c,d]: continue
                        for f in range(10):
                            if f in [a,b,c,d,e]: continue
                            for g in range(10):
                                if g in [a,b,c,d,e,f]: continue
                                for h in range(10):
                                    if h in [a,b,c,d,e,f,g]: continue
                                    if check(int(str(a)+str(b)+str(c)+str(d)+str(e)
                                              +str(f)+str(g)+str(h))):
                                        if check(int(str(b)+str(c)+str(d)+str(a)+str(e)
                                                     +str(f)+str(g)+str(h))):
                                            print("HOORAY!!!")

def chk_six():
    for a in range(1,10):
        for b in range(10):
            if b==a: continue
            for c in range(10):
                if c in [a,b]: continue
                for d in range(10):
                    if d in [a,b,c]: continue
                    for e in range(10):
                        if e in [a,b,c,d]: continue
                        for f in range(10):
                            if f in [a,b,c,d,e]: continue
                            if check(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))):
                                if check(int(str(f)+str(e)+str(a)+str(b)+str(c)+str(d))):
                                    print("HOORAY!!!")

def chk_five():
    for a in range(1,10):
        for b in range(10):
            if b==a: continue
            for c in range(10):
                if c in [a,b]: continue
                for d in range(10):
                    if d in [a,b,c]: continue
                    for e in range(10):
                        if e in [a,b,c,d]: continue
                        if check(int(str(a)+str(b)+str(c)+str(d)+str(e))):    #BOARD
                            if check(int(str(a)+str(d)+str(b)+str(c)+str(e))):#BROAD
                                print("HOORAY!!!")

chk_five()                                            
