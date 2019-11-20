a = 0
b = input()
c = raw_input().strip().split()

for i in xrange(b):
    a = a + int(raw_input().split()[c.index('MARKS')])

print float(a) / b
