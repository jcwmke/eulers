#If we list all the natural numbers below 10 that
#are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
###Find the sum of all the multiples of 3 or 5 below 1000.

target = 0
top = 1000
i = 1

while i < top:
    if i % 3 == 0:
        if i % 5 != 0:
            target = target + i
    if i % 5 == 0:
        target = target + i
    i = i + 1

print target
