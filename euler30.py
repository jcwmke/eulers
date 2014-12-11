##Surprisingly there are only three numbers that can be
##written as the sum of fourth powers of their digits:
##1634 = 14 + 64 + 34 + 44
##8208 = 84 + 24 + 04 + 84
##9474 = 94 + 44 + 74 + 44
##As 1 = 14 is not a sum it is not included.
##
##The sum of these numbers is 1634 + 8208 + 9474 = 19316.
##
##Find the sum of all the numbers that can be written as
##the sum of fifth powers of their digits.

i = 2
wholesum = 0

while i < 1000000:
    targetsum = 0
    j = str(i)
    for item in j:
        x = int(item)
        targetsum = x**5 + targetsum
    if targetsum == i:
        wholesum = wholesum + targetsum
        print targetsum
    i = i + 1

print wholesum
