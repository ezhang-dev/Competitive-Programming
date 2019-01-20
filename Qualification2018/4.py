import math
def solve():
	a = float(input())
	t = math.acos(a / (2 ** 0.5))
	ff = math.pi / 4
	v1 = [0.5 * math.cos(t + ff), 0.5 * math.sin(t + ff), 0]
	v2 = [0.5 * math.cos(t - ff), 0.5 * math.sin(t - ff), 0]
	v3 = [0, 0, 0.5]
	return '\n' + '\n'.join([' '.join(map(str, v)) for v in [v1, v2, v3]])
if __name__ == "__main__":
	for caseNr in range(1, int(input()) + 1):
		print("Case #%i: %s" % (caseNr, solve()))
