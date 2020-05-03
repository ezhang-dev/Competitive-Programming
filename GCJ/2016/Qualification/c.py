from math import sqrt
from itertools import count, islice
from fractions import gcd
import random
def solve(i):
	i=i.split()
	c=list()
	for x in range(0,int(i[1])):
		t=list()
		for y in range(0,10):
			t.append(None)
		c.append(t)
	seed=(1<<(int(i[0])-1))+1
	print(seed)
	z=0
	while z<int(i[1]) and seed<(1<<(int(i[0]))):
		n=bin(seed)[2:]
		c[z][0]=n
		z=p(n)
		seed=seed+2
		z=z+1
	z=0
	while z<int(i[1]):
		n=c[z][0]
		print(n)
		for x in range(2,11):
			c[z][x-1]=brent(int(n,x))
		z=z+1
	for x in range(0,int(i[1])):
		c[x]=' '.join(map(str,c[x]))
	c ='\n'+'\n'.join(map(str,c))
	return c
def p(n):
	for x in range(2,11):
		print(str(x)+" "+n)
		if isprime(int(n,x)):
			return -1
	return 0

def isprime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g    
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = raw_input()
        print("Case #%i: %s" % (caseNr, solve(info)))
