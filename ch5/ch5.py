'ch5 Files and I/O'


'Reading and Writing TextData'

"""
Problem

You need to read or write text data, possibly in different text encodings such as ASCII, UTF-8, or UTF-16.
"""

# with open(rt)

with open('C:/Users/STEVE/Documents/pycookbook/test.py') as f:
    data = f.read()
    #print(data)

# Iterate over the lines ...
with open('C:/Users/STEVE/Documents/pycookbook/test.py') as f:
    for line in f:
        print("\t" , line)


'Printing to a File'
with open('print_redirected.txt','wt') as f:
    print("This is a line", file = f)
    print("This is a new line", file = f)


'Printing with a Different Separator or Line Ending'

print("1","2","3", sep = '\t', end="**")

'Reading and Writing Binary Data'

###################### 'open(filename, rb) as f'

'Writing to a File That Doesn’t Already Exist'

'You want to write a new file. to avoid its already exist.'
#with open('somefile', 'xt') as f:
#...     f.write('Hello\n')


