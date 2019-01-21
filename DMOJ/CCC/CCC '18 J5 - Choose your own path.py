from collections import deque
m=int(input())
b=[]
for i in range(m):
	pg=list(map(lambda x:int(x)-1,input().split(" ")))[1:]
	b.append([False,pg])
q=deque()
q.append((0,1))
mm=-1
while q:
	pg,c=q.popleft()
	pg=b[pg]
	if pg[0]:
		continue
	pg[0]=True
	if len(pg[1])==0 and mm==-1:
		mm=c
	for i in pg[1]:
		q.append((i,c+1))
q='N' if len(list(filter(lambda x:not x[0],b[1:]))) > 0 else 'Y'
print(q)
print(mm)