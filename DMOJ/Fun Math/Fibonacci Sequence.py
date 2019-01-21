mod = 10 ** 9 + 7
n = int(input())
def f(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = f(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c % mod, d % mod)
        else:
            return (d % mod, (c + d) % mod)
print(f(n)[0])