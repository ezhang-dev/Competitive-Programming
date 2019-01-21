def r(n):
    n=str(n)
    b=""
    for a in n:
        if a=='0' or a=='1' or a=='8':
            b=a+b
        elif a=='6':
            b='9'+b
        elif a=='9':
            b='6'+b
        else:
            return False
    return n==b
def q(a,b):
    return sum(map(r,range(a,b+1)))
print(q(int(input()),int(input())))