z=int(input())
a=[int(i) for i in input().split(' ')]
a.sort()
b=[]
q=False
o=z%2
p=(z+1)%2
for s in range(0,z):
	if q:
		b.append(a[z//2+o])
		o=o+1
	else:
		b.append(a[z//2-p])
		p=p+1
	q=not q
print (" ".join([str(i) for i in b]))