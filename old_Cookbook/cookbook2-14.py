'2.14 Combining and Concatenating Strings '


parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print ' '.join(parts)

print ','.join(parts)

print ''.join(parts)


a = 'Is Chicago'
b = 'Not Chicago?'
print a + b

print 'Hello' " World"


c = 'I love python'

print (a+':'+b+':'+c)
# ugly


print ':'.join([a,b,c])
# still ugly

print (a,b,c, sep=":")
# Better, maybe in Python 3

