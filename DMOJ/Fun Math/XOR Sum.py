from functools import reduce 
input()
a = list(map(int,input().split(" ")))
print(sum(a)-reduce(lambda x,y:x^y,a,0))