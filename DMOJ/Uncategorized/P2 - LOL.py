xmin=ymin=9000
xmax=ymax=-9000
for _ in range(int(input())):
    a,b=map(int,input().split())
    xmin=min(xmin,a)
    xmax=max(xmax,a)
    ymin=min(ymin,b)
    ymax=max(ymax,b)
print((xmax-xmin)*(ymax-ymin))