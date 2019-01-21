def r13(s):
    if s>='a' and s<= 'z':
        q=(ord(s)-ord('a')+13)%26
        return chr(q+ord('a'))
    if s>='A' and s<= 'Z':
        q=(ord(s)-ord('A')+13)%26
        return chr(q+ord('A'))
    return s
for x in range(5):
    print(''.join(map(r13,input())))