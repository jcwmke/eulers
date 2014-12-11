##An irrational decimal fraction is created by concatenating the positive integers:
##0.123456789101112131415161718192021...
##It can be seen that the 12th digit of the fractional part is 1.
##If dn represents the nth digit of the fractional part, find the value of the following expression.
##d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

i = 1
k = 1
targetprod = 1
x = "0"
listed = []

for i in range(1,1000000):
    j = str(i)
    x = x + j

while k <= 1000000:
    targetprod = targetprod * int(x[k])
    k = k * 10

print targetprod

    
    




    
