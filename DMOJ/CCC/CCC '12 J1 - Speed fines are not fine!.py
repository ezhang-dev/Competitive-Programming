a=input()
b=input()
c=b-a
if c<1:
    print"Congratulations, you are within the speed limit!"
elif c<21:
    print"You are speeding and your fine is $100."
elif c<31:
    print"You are speeding and your fine is $270."
else:
    print"You are speeding and your fine is $500."