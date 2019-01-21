z=int(input())
a=[int(i) for i in input().split(' ')]
b=[int(i) for i in input().split(' ')]
c=0
d=0
q=-1
for x in range(0,z):
	c=c+a[x]
	d=d+b[x]
	if c==d:
		q=x
print (q+1)