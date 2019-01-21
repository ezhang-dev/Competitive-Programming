g = """*x*
 xx
* *""".split("\n")
n = int(input())
g = sum(map(lambda x: [''.join(map(lambda y: y * n, list(x)))] * n, g), [])
print('\n'.join(g))