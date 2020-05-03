from collections import Counter

def solve():
    input()
    c = Counter()
    d = Counter()
    s = set()
    for _ in range(10**4):
        a,b = input().split()
        i = len(b)
        d.update(b)
        for x in b:
            c[x]=c[x]+i**3
            i = i-1
            break
        s.add(b[0])
    x = list(map(lambda x:x[0],c.most_common()))
    xx = list(map(lambda x:x[0],d.most_common()))
    zz = set(xx).difference(s).pop()
    #x.remove(zz)
    return zz+''.join(x)


for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
