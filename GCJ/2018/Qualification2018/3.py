def runA():
	p = set([(x, y) for x in [1, 2, 3, 4] for y in [1, 2, 3, 4, 5]])
	v = set([(2, 2), (3, 2), (2, 4), (3, 4)])
	while p:
		for vv in v:
			if cover(p, *vv):
				continue
			print(str(vv[0]) + ' ' + str(vv[1]))
			q, w = map(int, input().split())
			if q == w and (q == 0 or q == -1):
				return
			if (q, w) in p:
				p.remove((q, w))
def runB():
	p = set([(x, y) for x in range(1,11) for y in range(1,21)])
	v = set([(x, y) for x in [2,5,8,9] for y in [2,5,8,11,14,17,19]])
	while p:
		for vv in v:
			if cover(p, *vv):
				continue
			print(str(vv[0]) + ' ' + str(vv[1]))
			q, w = map(int, input().split())
			if q == w and (q == 0 or q == -1):
				return
			if (q, w) in p:
				p.remove((q, w))
def run():
	if input()=='20':
		runA()
	else:
		runB()
def cover(p, x, y):
	for s in [(a, b) for a in [x-1, x, x+1] for b in [y-1, y, y+1]]:
		if s in p:
			return 0
	return 1
for _ in range(int(input())):
	run()