import collections
class node():
    dist=0
    id=(1,1)
v=set()
td=collections.deque()
n=node()
n.id=tuple(map(int,input().split()))
td.append(n)
t=tuple(map(int,input().split()))
while True:
    n=td.popleft()
    id=n.id
    if id==t:
        print(n.dist)
        break
    if id in v:
        continue
    v.add(id)
    if id[0]<8 and id[1]<7:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]+1,id[1]+2)
        td.append(q)
    if id[0]<7 and id[1]<8:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]+2,id[1]+1)
        td.append(q)
    if id[0]>1 and id[1]<7:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]-1,id[1]+2)
        td.append(q)
    if id[0]<7 and id[1]>1:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]+2,id[1]-1)
        td.append(q)
    if id[0]>1 and id[1]>2:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]-1,id[1]-2)
        td.append(q)
    if id[0]>2 and id[1]>1:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]-2,id[1]-1)
        td.append(q)
    if id[0]<8 and id[1]>2:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]+1,id[1]-2)
        td.append(q)
    if id[0]>2 and id[1]<8:
        q=node()
        q.dist=n.dist+1
        q.id=(id[0]-2,id[1]+1)
        td.append(q)