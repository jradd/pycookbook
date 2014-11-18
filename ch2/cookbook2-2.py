'2.2 Matching Text at the start or end of a String'

"""
Problem

You need to check the start or end of a string for specific text patterns, such as filename extensions, URL schemes, and so on.

Talk about startswith() and endswith() function.
"""

url ='http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
print(filenames)

'None'
print([no_python for file in filenames if not file.endswith('py')])

import urllib
def read_data(name):
	if name.startswith( ('http:', 'https:', 'ftp:')):
		return urllib.urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()


if any (name.endswith( ('.c', '.py')) for name in os.listdir('.') ):
	print('c , or python found!')