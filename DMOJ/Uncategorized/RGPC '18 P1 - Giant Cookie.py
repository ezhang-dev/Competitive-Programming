a,b=map(int,input().split())
if a%b==0:
    print("yes "+str(a//b))
else:
    f=1
    g=b
    while f:
       g+=1
       f=a%g
    print("no "+str(g-b))