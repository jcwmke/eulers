##The Fibonacci sequence is defined by the recurrence relation:
##Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
##The 12th term, F12, is the first term to contain three digits.
##What is the first term in the Fibonacci sequence to contain 1000 digits?

x = 1
y = 1
z = x + y
termcounter = 3 #values 1,1 indicate we're generating the third term first
length = 0

while length <= 1000:
    z = x + y
    x = y
    y = z
    length = len(str(z))
    if length == 1000:
        print termcounter
        break
    termcounter = termcounter + 1

    
    
