import sys

def solve():
	(r,c, h, v)=map(int,input().split(" "))
	cake=[]
	for z in range(0,r):
		cake.append(list(map(lambda x: x == '@', input())))
	chips = ss(cake)
	if chips % ((h + 1) * (v + 1)) != 0:
		return 'IMPOSSIBLE'
	if chips == 0:
		return 'POSSIBLE'
	cps = chips // (((h + 1) * (v + 1)))
	hs = cs(cake, cps * (v + 1)) 
	vs = cs(list(zip(*cake[::-1])),  cps * (h + 1))
	vv = len(hs) == h + 1 and len(vs) == v + 1
	return 'POSSIBLE' if  ccheck(cake, hs, vs, cps) and vv else 'IMPOSSIBLE'
def ss(cake):
	s = 0
	for _ in cake:
		s += sum(_)
	return s
def cs(cake, cps):
	l = []
	i = 0
	for _ in range(0, len(cake)):
		i += sum(cake[_])
		if i == cps:
			i = 0
			l.append(_)
	return l
def scheck(cake, hs):
	c = []
	hs = [-1] + hs
	for i in range(len(hs) - 1):
		c.append(cake[hs[i]+1:hs[i+1]+1])
	
	return c
def ccheck(cake, hs, vs, cpsz):
	global cps
	cps = cpsz
	c = scheck(cake, hs)
	for _ in c:
		z = scheck(list(zip(*_[::-1])), vs)
		if list(filter(lambda x: ss(x) != cps, z)):
			return False
	return True
if __name__ == "__main__":
	testcases = int(input())
	for caseNr in range(1, testcases + 1):
		print("Case #%i: %s" % (caseNr, solve()))
