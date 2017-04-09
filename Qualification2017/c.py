import sys
import heapq
def solve(info):
	(n,k)=map(int,info.split(" "))
	s=[]
	heapq.heappush(s,-n)
	pi=0
	for _ in xrange(0,k):
		pi=-heapq.heappop(s)
		heapq.heappush(s,-1*((pi-1)//2))
		heapq.heappush(s,-(pi//2))
		#print((i,s))
	return str(pi//2)+' '+str((pi-1)//2)

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		sys.stderr.write(str(caseNr)+'\n')
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))