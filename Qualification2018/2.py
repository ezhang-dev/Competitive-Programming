import sys
input = sys.stdin.readline
def solve():
	v = int(input())
	nums = 0
	a = []
	b = []
	for i in map(int, input().split()):
		(a, b)[nums % 2].append(i)
		nums += 1
	a.sort()
	b.sort()
	nums = [0] * v
	nums[::2] = a
	nums[1::2] = b
	for i in range(v - 1):
		if nums[i] > nums[i+1]:
			return i
	return 'OK'
if __name__ == "__main__":
	for caseNr in range(1, int(input()) + 1):
		print("Case #%i: %s" % (caseNr, solve()))
