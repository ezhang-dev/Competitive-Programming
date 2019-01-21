one=True
two=one<<one
four=one<<two
five=four+one
six=two+four
seven=six+one
eight=two<<two
C=eight+four
sixteen=one<<four
F=sixteen-one

s=map(chr,[four*sixteen+eight,six*sixteen+five,six*sixteen+C,six*sixteen+C,six*sixteen+F,two*sixteen+C,two*sixteen,five*sixteen+seven,six*sixteen+F,seven*sixteen+two,six*sixteen+C,six*sixteen+four,two*sixteen+one])
print(str().join(s))