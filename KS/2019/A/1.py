def solve(info):
	n, p = map(int, info.split())
	i = sorted(map(int, input().split()))
	top = i[p-1]
	time = sum([top - i[x]  for x in range(0, p - 1)])
	timemax = time
	for x in range(p, n):
		ntime = time - (top - i[x-p])
		ntime = ntime + (i[x] - top) * (p - 1)
		top = i[x]
		time = ntime
		timemax = min(timemax, ntime)
	return timemax
if __name__ == "__main__":
	testcases = int(input())
	for caseNr in range(1, testcases + 1):
		info = input()
		print("Case #%i: %s" % (caseNr, solve(info)))
