def base(x,y):
    if (x in [1,2,3] and y==0) or (x==2 and y==1):
        return 1
    if (x in [1,3] and y==1) or (x==2 and y==2):
        return 2
    return 0

def rec(m,x,y):
    off=5**(m-1)
    l=base(x//off,y//off)
    if m==1 or l==1:
        return l==1
    if l==0:
        return False
    return rec(m-1,x%off,y%off)

for i in range(int(input())):
    m,x,y=map(int,input().split())
    print('crystal' if rec(m,x,y) else 'empty')