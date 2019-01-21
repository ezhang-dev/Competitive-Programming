p=[2]+(lambda s,r=range:[[[s.__setitem__(y,0)for y in r(x*x,len(s),x)]for x in r(3,len(s),2)if s[x]],[i for i in r(3,len(s))if s[i]]][1])([0,1]*(10000//2))
import bisect
input()
for _ in map(int,input().split()):
    i = bisect.bisect_left(p, _) - 1
    print('no can do' if _ < 3 else p[i])