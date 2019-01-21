def s():
	n, m = map(int, input().split())
	dec = {}
	for _ in 'a' * 4:
		k, v = input().split()
		dec[k] = v
	p = list(input())
	q = []
	for _ in range(m - 1):
		for i in range(n):
			q.append(dec[p[(i-1+n)%n]+p[(i+1+n)%n]])
		p = q
		q = []
	input()
	return ''.join(p)
for _ in range(10):
	print(s())