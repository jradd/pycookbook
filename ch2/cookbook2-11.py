'2.11 Strip Unwanted Characters from Strings'

# Whitespace stripping

s = '   hello world \n'

print s.strip()

# lstrip, rstrip , perform stripping from the left  right side


# Characters stripping

t= '---hello world ===='

print t.strip('-= ')



# inner space

asstring  = 'hello          world'

print asstring.replace('  ', '')
import re
print re.sub('\s+', ' ', asstring)

