import networkx as nx

def solve(info):
	n=int(info)
	G=nx.DiGraph()
	G.add_nodes_from(range(n))
	f=map(lambda x: int(x)-1,raw_input().split(' '))
	for i,r in enumerate(f):
		G.add_edge(i,r)
	#Return a list of cycles described as a list o nodes
	all_cycles = list(nx.simple_cycles(G))
	te=[]
	#Find longest cycle
	clen = 0
	for cycle in all_cycles:
		cycle_len = len(cycle)
		if cycle_len == 2:
			te.append(cycle)
		if cycle_len>clen:
			clen = cycle_len
	p=[0]*n	
	for x in range(n):
		cur=x
		vis=[False]*n
		l=0
		while not vis[cur]:
			vis[cur]=True
			l=l+1
			cur=f[cur]
		p[cur]=max(p[cur],l)
	tot=0	
	for (i,j) in te:
		tot+=p[i]+p[j]-2
	return max(tot,clen)
	

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))
