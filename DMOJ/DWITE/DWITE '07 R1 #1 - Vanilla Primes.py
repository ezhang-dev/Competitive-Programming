i=int(input())
if i<=1:
    print("not")
elif i==2:
    print("prime")
else:
    q=True
    for x in range(2,int(i),1):
        if i%x==0:
            q=False
    print("prime" if q else "not")