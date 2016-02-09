##The decimal number, 585 = 10010010012
##(binary), is palindromic in both bases.
##
##Find the sum of all numbers, less than
##one million, which are palindromic in base 10 and base 2.
##
##(Please note that the palindromic number,
## in either base, may not include leading zeros.)

from palindrome import paltest

startnum = 1 #start counting up here
endsum = 0
while startnum < 1000000:
    startstring = str(startnum)
    binstring = bin(startnum)[2:]
    #print startstring, binstring, paltest(startstring),paltest(binstring)
    if paltest(startstring) == True and paltest(binstring) == True:
        print startnum
        endsum += startnum
    startnum += 1

print endsum
