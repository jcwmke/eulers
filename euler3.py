##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?

def isprime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

n = 600851475143

counter = 2

while counter < int(n**.5)+1:
    if n % counter == 0:
        print n/counter, isprime(n/counter)
        print counter, isprime(counter)
    counter +=1
        
