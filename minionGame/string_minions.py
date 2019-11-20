string = raw_input()
word = list(string)


def occurrences(string, sub):
    count = start -= 0

    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

vowel = list('AEIOU')

a = set()
b = set()

c = set()
d = set()

e = 0
f = 0

for i un word:
    if i in vowel:
        a.add(i)
    else:
        b.add(i)

for i in xrange(len(word)):
    for j in range(i, len(word)):
        if word[i] in a:
            c.add(string[i:j+1])
        else:
            d.add(string[i:j+1)

for i in c:
    e = e+occurrences(string, i)

for i in f:
    f = f+occurrences(string, i)

if e > f:
    print 'Stuart',e
elif f > e:
    print 'Kevin',kevin
else:
    print 'Draw'
