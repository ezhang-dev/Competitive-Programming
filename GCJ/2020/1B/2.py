import sys

def cin():
    out = input()
    if out == "CENTER":
        raise ValueError()
    if out == "WRONG":
        sys.exit(1)
    return out == "HIT"

def search(a,b,f,axisX,direction):
    while a != b:
        m = (a + b) //2
        if axisX:
            print(m,f)
        else:
            print(f,m)
        if cin():
            if direction:
                if a == m:
                    return m
                a = m
            else:
                if b==m:
                    return m
                b = m
        else:
            if direction:
                if b == m:
                    return m
                b = m
            else:
                if a == m:
                    return m
                a = m
    return a
def solve():
    z= 10**9
    x,y =0,0
    print(0,0)
    if cin():
        x,y = 0,0
    print(z//2,z//2)
    if cin():
        x,y = z//2,z//2
    print(z//2,-z//2)
    if cin():
        x,y = z//2,-z//2
    print(-z//2,z//2)
    if cin():
        x,y = -z//2,z//2
    print(-z//2,-z//2)
    if cin():
        x,y = -z//2,-z//2
    a = search(x,z,y,True,True)
    b = search(-z,x,y,True,False)
    p = (a+b)//2
    m = search(y,z,p,False,True)
    n = search(-z,y,p,False,False)
    o = (m+n)//2
    for mm in [-1,0,1]:
        for nm in [-1,0,1]:
            print(p+mm,o+nm)
            cin()
x,y,z = map(int,input().split())
print(x, file=sys.stderr)
for _ in range(x):
    try:
        solve()
    except ValueError:
        continue
    
    
