'Chapter 5 File and I.O'

# read file once
# with open('test.csv', 'r') as f:
# 	data = f.read()
# 	print(data)

# or it's better to read by line.

with open('test.csv','r') as f:
	for line in f:
		print("One line", line, end='')




# Simple File Write

# with open('test_write.txt','w') as f:
# 	f.write("this is first line")
# 	f.write("this is secodn line, i am a writer? LOL")

# Redirected Print statement.


# old content is gone. flushed by the new content.
with open('test_write.txt','w') as f:
	print("this is first line file = f\n", file = f)
	print("this is secodn line, i am a writer? LOL file = f",file = f)




# about encoding.  use argument.
# with open('somefile.txt', 'rt', encoding='latin-1') as f:



# about difference between Unix and Windows

# Another minor complication concerns the recognition of newlines, which are different on Unix and Windows (i.e., \n versus \r\n).


'6.2 Printing to a File'

# with open('somefile.txt', 'rt') as f:
#     print('Hello World!', file=f)


'6.3 Printing with a Different Separator or Line Ending'
print('\n\n')
print('ACME', 60, 91.5)
print('ACME', 60, 91.5, sep='*', end='>>>')


row= ('ACME', 60, 91.5)
print(row, sep="**") # no separate,  because row is one entity
print(*row, sep="**")  # row become a list (can be sperated.)
