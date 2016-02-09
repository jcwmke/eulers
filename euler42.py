##The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
##so the first ten triangle numbers are:
##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##By converting each letter in a word to a number corresponding to
##its alphabetical position and adding these values we form a word value.
##For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
##If the word value is a triangle number then we shall call the word a triangle word.
##Using words.txt (right click and 'Save Link/Target As...'),
##a 16K text file containing nearly two-thousand
##common English words, how many are triangle words?

wordlist = open('c:/users/charlie/downloads/wordlist.txt')
x = wordlist.read()
y = x.split('"')
for i in y:
    if ',' in i or len(i) == 0:
        y.remove(i)
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
trianglewords = 0

#generates list of triangle numbers to cross reference
trianglelist = []
m = 1
while m < 20:
    trianglelist.append((m+1)*m*.5)
    m = m + 1    

for word in y:
    target = 0
    for k in word:
        value = alphabet.index(k) + 1
        target = target + value
    for j in trianglelist:
        if j == target:
            trianglewords = trianglewords + 1

print trianglewords
wordlist.close()
