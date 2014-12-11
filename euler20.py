##n! means n × (n − 1) × ... × 3 × 2 × 1
##
##For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
##and the sum of the digits in the number 10!
##is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
##
##Find the sum of the digits in the number 100!

i = 100 #the number to be factorial-ed
x = 1 #iterator
targetsum = 0

#product of the factored #
while i > 1:
    x = x * i
    i = i - 1
y = str(x)

#sum of the numbers of the product
a = 0
while len(y) > 0:
    z = int(y[a])
    targetsum = targetsum + z
    y = y[1:]

print targetsum
    
