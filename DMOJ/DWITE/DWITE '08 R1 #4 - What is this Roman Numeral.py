r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for _ in range(5):
    tot = prev = 0
    for l in list(input())[::-1]:
        if prev > r[l]:
            tot -= r[l]
        else:
            tot += r[l]
        prev = r[l]
    print(tot)