// Sorry but dont rember what problem set this is from
def main():
	z=int(input())
	x=0
	while x<z:
		l=j1()
		print("Case #"+str(x+1)+": "+str(l))
		x=x+1
	return 0
def j1():
	i=input()
	i=i.split()
	r=int(i[0])
	t=int(i[1])
	ri=0
	c=0
	a=1
	while True:
		c=2*(r+a)-1
		if c>t:
			break
		t=t-c
		ri=ri+1
		a=a+2
	return ri
if __name__ == '__main__':
		main()