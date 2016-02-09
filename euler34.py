##145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##Find the sum of all numbers which are equal to the
##sum of the factorial of their digits.
##
##Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#checks whether the sum of the factors of x is equal to x itself
def factors(x):
    endsum = 0
    for i in list(str(x)):
        endsum += factorial(int(i))
    if endsum == x: return x
        
#factorial function
def factorial(x):
    target = 1
    while x > 0:
        target *= x
        x += -1
    return target


counter = 0
while counter < 2000000:
    factors(counter)
    counter += 1

