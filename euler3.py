##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?
from primeness import isprime

n = 600851475143

counter = 2

while counter < int(n**.5)+1:
    if n % counter == 0:
        print n/counter, isprime(n/counter)
        print counter, isprime(counter)
    counter +=1

isprime(7)
isprime(11)
