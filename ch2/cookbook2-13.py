'2.13 Aligning Text Strings'

# format text with some sort of alignment applied

# solution :  ljust()  rjust()  and center()



text = 'Hello World'

print text.ljust(20)
print text.rjust(20)
print text.center(20)

print text.rjust(20, '=')
print text.center(20, '=')




print format(text, '>20')
print format(text, '<20')
print format(text, '^20')

print format(text,'*>20s')
print format(text,'*^20s')

print '{:>10s} {:>10s}'.format('Hello', 'World')

# format work floats

x = 1.2345

print format(x, '>10')
print format(x, '^10.2f')



# % operator

print '%-20s' % text

print '%20s' % text


# love format function, hope so.