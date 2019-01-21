from collections import deque
input()
q=deque()
i=1
for x in input():
    if x=='0':
        q.append(i)
    else:
        q.appendleft(i)
    i+=1
print('\n'.join(map(str,q)))