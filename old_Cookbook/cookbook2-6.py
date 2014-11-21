'2.6 Searching and Replacing Case-insensitive text'

text = 'UPPER PYTHON, lower python, Mixed Python'

import re
print re.findall('python', text, flags =re.IGNORECASE)

print re.sub('python', 'snake', text, flags= re.IGNORECASE)

def matchcase(word):
	def replace(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		elif text.islower():
			return word.lower()
		elif text[0].isupper():
			return word.capitalize()
		else:
			return word
	return replace

print re.sub('python', matchcase('snake'), text, re.I)

"""
Discussion

For simple cases, simply providing the re.IGNORECASE is enough to perform case-insensitive matching. However, be aware that this may not be enough for certain kinds of Unicode matching involving case folding. See “Working with Unicode Characters in Regular Expressions” for more details.
"""