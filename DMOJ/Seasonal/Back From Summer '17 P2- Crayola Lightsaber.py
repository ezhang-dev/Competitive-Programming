import collections
i=int(input())
c=collections.Counter(input().split())
t=c.most_common(1)[0][1]
print(min(t,i-t+1)+i-t)