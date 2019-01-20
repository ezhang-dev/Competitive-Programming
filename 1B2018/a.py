import sys
import math
def solve():
	(N, L)=map(int,input().split())
	k = list(map(int, input().split()))
	k = k + [0] * (L - len(k))
	j = 0
	l = []
	m = 0
	print(k)
	for i in k:
		d = math.ceil((math.floor(i / N * 100) + 0.5) * N)
		p =  d - i * 100
		l.append(max(p, 0))
		j += i
		m += math.floor(i / N * 100)
	d = N - j
	m += math.floor(d / N * 100)
	print(l)
	l.sort()
	for i in l:
		print(m)
		if d < i:
			break		
		d -= i
		m += 1 + math.floor(i / N * 100)


	return m

if __name__ == "__main__":
	testcases = int(input())
	for caseNr in range(1, testcases + 1):
		print("Case #%i: %s" % (caseNr, solve()))
