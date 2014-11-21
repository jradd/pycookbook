'2.3 Matching Strings Using Shell Wildcard Pattern'

from fnmatch import fnmatch, fnmatchcase

print fnmatch('foo.txt', '*.txt')
print fnmatch('foo.txt', '?oo.txt')
print fnmatch('afoo.txt', '?oo.txt')
print fnmatch('Dat34.csv', 'Dat[0-9]*.csv')



# care.  On OS X (Mac)

print fnmatch('foo.txt', '*.TXT') # False
print fnmatch('foo.txt', '*.TXT') # True


# to avoid it use fnmatchcase

print fnmatchcase('foo.txt', '*.TXT') # False for windows

address = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print [addr for addr in address if fnmatchcase(addr, '* ST')]
print [addr for addr in address if fnmatchcase(addr, '* AVE')]

print [addr for addr in address if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

