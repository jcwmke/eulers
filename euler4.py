##A palindromic number reads the same both ways. The largest
##palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
##Find the largest palindrome made from the product of two 3-digit numbers.

targetnum = 0

for i in range(100,999):
    for j in range(100,999):
        c = i*j
        d = str(c)
        if len(d) == 6 and d[0] + d[1] + d[2] == d[5] + d[4] + d[3]:
            if c > targetnum:
                targetnum = c
    
print targetnum
