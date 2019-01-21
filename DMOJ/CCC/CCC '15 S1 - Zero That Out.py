q=[]
for z in range(int(input())):
    a=int(input())
    if a==0:
        q.pop()
    else:
        q.append(a)
print(sum(q))