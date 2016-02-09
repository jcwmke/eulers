##By listing the first six prime numbers:
##2, 3, 5, 7, 11, and 13, we can see
##that the 6th prime is 13.
##
##What is the 10,001st prime number?

primeset=[2,3,5]
i = 7
prime = True
j = 1
a = 1
y = 1
targetno = 3

#primetester
while  len(primeset) < 10001:
    for x in primeset:
        if i % x == 0:
            prime = False
        if x > i**.5:
            break
    if prime == True:
        primeset.append(i)       
    prime = True
    i = i + 2

print len(primeset), primeset[-1]
            
