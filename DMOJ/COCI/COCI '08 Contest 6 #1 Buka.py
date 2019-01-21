a=len(input())-1
op=input()
b=len(input())-1
if op=="*":
    print("1"+"0"*(a+b))
else:
    q=min(a,b)
    r=max(a,b)
    if q==r:
        print("2"+"0"*q)
    else:
        print("1"+"0"*(r-q-1)+"1"+"0"*q)