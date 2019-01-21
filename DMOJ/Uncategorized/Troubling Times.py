n,d=map(int,input().split())
q=min(map(lambda x:abs(d//int(x)) if d%int(x)==0 else 99999,input().split()))
print(q if q!=99999 else 'This is not the best time for a trip.')