n = int(input())
if n == 1:
    print( 1)
else:
    cos = [1, 1, 0, -1, -1, -1, 0, 1]
    mod = 10 ** 9 + 13
    a = pow(2, n - 2, mod)
    b = pow(2, n // 2 - 1, mod)
    c = cos[n%8]
    
    print((a + b * c) % mod)