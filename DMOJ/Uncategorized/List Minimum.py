i=int(input())
b=[]
for x in range(i):
    b.append(int(input()))
b.sort()
print('\n'.join(map(str,b)))