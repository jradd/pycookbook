#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:

"""


'Reading Writing binary File'

'read mode or write mode turns.  "rb"  "wb" '




"""  book instance

# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()
    # and here you can do some encoding. decoding work
    text = data.encode('utf-8')

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

"""

'Write a file that does not exist '

'You want to write data to a file, but only if it doesn’t already exist on the filesystem.'
' Just write a new file to system. '
# This problem is easily solved by using the little-known x mode to open() instead of the usual w mode. For example:


'Performing I.O Operations on s string'

import io
s = io.StringIO()

# write in.. <<
s.write("hi, my name is jyjdsaf")
print("this is a testoool;  ", file = s)
#get out all data written so far.

print(s.getvalue())



# read out <<
s = io.StringIO('Hello \r\t This is yjy speaking. \r\t' )
print(s.read(10) )
print(s.read())


# The io.StringIO class should only be used for text. If you are operating with binary data, use the io.BytesIO class instead. For example:



# binary .

"""  book instance
>>> s = io.BytesIO()
>>> s.write(b'binary data')
>>> s.getvalue()
b'binary data'
>>>
"""

'Reading and Writing Compressed Datafiles'
'pass'



' Iterating over fixed-sized Record'

from functools import partial

RECORD_SIZE = 32

with open('test.csv', 'rb') as f:
	records = iter(partial(f.read, RECORD_SIZE), b'')
	for r in records:
		print(r)
		print("one record_size is output.")



'Reading Binary Data into a Mutable Buffer'

import os.path
def read_into_buffer(filename):
	buf = bytearray(os.path.getsize(filename))
	with open(filename, 'rb') as f:
		f.readinto(buf)
	return buf

# Write a sample file
with open('sample.bin', 'wb') as f:
	f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)

with open('newsample.bin','wb') as f:
	f.write(buf)