import sys

def solve():
	(n, p)=map(int,input().split(" "))
	q = 0
	cc = []
	df = 0
	zif = 0
	for _ in range(n):
		x, y = map(int,input().split(" "))
		p -= (x + y) * 2
		q += (x + y) * 2
		cc.append((2 *min(x, y), 2 * ((x ** 2 + y ** 2) ** 0.5)))
	cc.sort(key= lambda x: x[0])
	for _ in cc[::-1]:
		if p == 0:
			break
		if _[0] > p:
			continue
		if _[0] <= p:
			q += _[0]
			p -= _[0]
		df += _[1] - _[0]
	q += min(df, p)
	return q
if __name__ == "__main__":
	testcases = int(input())
	for caseNr in range(1, testcases + 1):
		print("Case #%i: %s" % (caseNr, solve()))
