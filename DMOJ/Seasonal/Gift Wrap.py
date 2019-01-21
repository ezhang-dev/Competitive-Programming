let='abcdefghijklmnopqrstuvwxyz'
wrap=['a']
n=int(input())
for x in range(n-1):
    wrap=list(map(lambda q:let[x+1]+q+let[x+1],wrap))
    wrap.insert(0,let[x+1]*(3+2*x))
    wrap.append(let[x+1]*(3+2*x))
print('\n'.join(wrap))