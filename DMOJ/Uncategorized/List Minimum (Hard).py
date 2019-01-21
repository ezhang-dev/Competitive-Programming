q=[]
for _ in xrange(input()):
    q.append(input())
q.sort()
print '\n'.join(map(str,q))