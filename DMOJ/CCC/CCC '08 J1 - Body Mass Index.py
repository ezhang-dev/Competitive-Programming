a=float(input())
b=float(input())
c=a/(b**2)
if c>25:
    print("Overweight")
elif c<18.2:
    print("Underweight")
else:
    print("Normal weight")