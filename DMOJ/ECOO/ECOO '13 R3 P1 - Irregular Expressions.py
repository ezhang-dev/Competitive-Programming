def s():
	e, *t = input().split()
	print(' '.join([m(e, x) for x in t]))
def m(a, b):
	#print(a, b)
	i = 0
	qq = []
	ads = 0
	for q in a:
		if i >= len(b):
			return "false"
		if ads:
			if q == ']':
				s = (len(qq) + 1) // 2
				if i + s > len(b):
					return "false"
				for z in b[i:i+s]:
					if z in qq:
						qq.remove(z)
					else:
						return "false"
				ads = False
				qq = []
				i += s
				continue
			qq.append(q)
		else:
			if q == '[':
				ads = 1
			else:
				if q != b[i]:
					return "false"
				i += 1
	return "true" if i == len(b) else "false"
for _ in range(10):
	s()