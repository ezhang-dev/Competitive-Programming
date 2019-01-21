x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
d=int(input())**2
print('Yes' if ((x1-x3)**2+(y1-y3)**2<=d or (x2-x3)**2+(y2-y3)**2<=d) else 'No')