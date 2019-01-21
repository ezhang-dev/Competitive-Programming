from functools import reduce

q=[]
for _ in range(int(input())):
    q.append(int(input()))
q.sort()
p=list(filter(lambda x:x>0,q))
m=list(filter(lambda x:x<0,q))
z=list(filter(lambda x:x==0,q))
pp=reduce((lambda x, y: x * y),p,1)
mm=reduce((lambda x, y: x * y),m,1)
if mm<0:
    mm//=m[-1]
if len(m)+len(p)==0:
  pp=0
if len(m)==1 and len(p)==0:
    pp=1
    if len(z):
        pp=0
    mm=m[0]
print(pp*mm)