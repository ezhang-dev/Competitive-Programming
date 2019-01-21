a=input()
map={}
map.update(zip(input(),a))
print(''.join([map.get(x,'.') for x in input()]))