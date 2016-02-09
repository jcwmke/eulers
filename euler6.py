# -*- coding: utf-8 -*-
##The sum of the squares of the first ten natural numbers is,
##
##12 + 22 + ... + 102 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)2 = 552 = 3025
##Hence the difference between the sum of the squares
##of the first ten natural numbers and the square of the
##sum is 3025 − 385 = 2640.
##
##Find the difference between the sum of the squares of
##the first one hundred natural numbers and the square of the sum.

def sumofsquares(num):
    counter = 0
    endsum = 0
    while counter <= num:
        endsum += counter**2
        counter += 1
    return endsum

def squareofsums(num):
    counter = 0
    endsum = 0
    while counter <= num:
        endsum += counter
        counter += 1
    return endsum**2

print squareofsums(100) - sumofsquares(100)
