import sys

def solve():
	(r, b, c)=map(int,info.split(" "))
	out = []
	for z in range(0, c):
		(m, s, p)=map(int,info.split(" "))
		out.append((m, s, p))
	out.sort(key = lambda x: x[0])
	rect=[]
	for row in range(0,r):
	return '\n'+pr(expand(rect,r,c),cake)

def rec(b, data):
	if b == 0:
		return 0
	z = []
	for s in range(len (data)):
		m, s, p = data[s]
		for i in range(1, b + 1):
			z.append(max(i * s + p, rec(b - 1), data[:s] + data[s+1:] ))

if __name__ == "__main__":
	testcases = int(input())
	for caseNr in range(1, testcases + 1):
		print("Case #%i: %s" % (caseNr, solve()))
