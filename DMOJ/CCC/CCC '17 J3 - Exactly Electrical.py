a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=int(input());
c=c-abs(a[0]-b[0])-abs(a[1]-b[1])
if c%2==0 and c>=0:
    print("Y")
else:
    print("N")