import sys

t,b =map(int,input().split())

for _ in range(t):
    left = ['']*(b//2)
    right = ['']*(b//2)
    p = [-1,'']
    d = [-1,'']
    i = 0
    q = 0
    while i < b//2:
        if q%10 == 0:
            if p[0]!=-1:
                q=q+1
                print(p[0])
                if input()!=p[1]:
                    left = ["0" if x == "1" else "1" for x in left]
                    right = ["0" if x == "1" else "1" for x in right]
                    p[1] = "0" if p[1] == "1" else "1"
                    d[1] = "0" if d[1] == "1" else "1"
            if d[0]!=-1:
                q=q+1
                print(d[0])
                if input()!=d[1]:
                    left,right=right,left
                    d[1] = "0" if d[1] == "1" else "1"
            if q%2==1:
                q=q+1
                print(1)
                input()
        print(i+1)
        l = input()
        print(b-i)
        r = input()
        q=q+2
        if p[0]==-1 and l == r:
            p=[i+1,l]
        if d[0]==-1 and l != r:
            d=[i+1,l]
        left[i]=l
        right[i]=r
        i=i+1
    out="".join(left+right[::-1])
    print(out)
    if "N"==input():
        sys.exit(1)
