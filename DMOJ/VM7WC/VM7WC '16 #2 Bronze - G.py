g = """GGGGG
G....
G..GG
G...G
GGGGG""".split("\n")
n = int(input())
g = sum(map(lambda x: [''.join(map(lambda y: y * n, list(x)))] * n, g), [])
print('\n'.join(g))