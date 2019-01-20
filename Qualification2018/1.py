def solve():
	d, cmd = input().split()
	d = int(d)
	cmd = cmd.rstrip('C')[::-1]
	i = 0
	while run(cmd[::-1]) > d and 'SC' in cmd:
		cmd = cmd.replace('SC', 'CS', 1).lstrip('C')
		i += 1
	return i if run(cmd[::-1]) <= d else 'IMPOSSIBLE'
def run(s):
	b = 1
	t = 0
	for _ in s:
		if _ == 'C':
			b *= 2
		else:
			t += b
	return t
if __name__ == "__main__":
	for caseNr in range(1, int(input()) + 1):
		print("Case #%i: %s" % (caseNr, solve()))
