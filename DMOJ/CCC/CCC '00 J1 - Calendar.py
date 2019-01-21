a, b = map(int, input().split())
c = [''] * (a - 1) + list(map(str, range(1, b + 1)))
c = list(map(lambda x: x.rjust(3), c))
c = [' '.join(c[i:i + 7]) for i in range(0, len(c), 7)]
print("Sun Mon Tue Wed Thr Fri Sat")
[print(i) for i in c]