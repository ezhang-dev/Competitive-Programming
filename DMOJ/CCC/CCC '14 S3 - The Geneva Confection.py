import sys
input = sys.stdin.readline
for _ in range(int(input())):
    p=[]
    i=0
    s=[]
    for __ in range(int(input())):
        s.append(int(input()))
    for j in s[::-1]:
        if j==i+1:
            i+=1
        else:
            if len(p)!=0 and p[-1]<j:
                break
            p.append(j)
        while len(p)!=0 and p[-1]==i+1:
            p.pop()
            i+=1
    print('Y' if len(p)==0 else 'N')