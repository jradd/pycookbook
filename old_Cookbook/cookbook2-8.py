'2.8 Writing a Regular Expression for Multiline Patterns'
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'

text2 = """
/* this is a
	multiline comment
	*/
	"""

print(comment.findall(text1))
print(comment.findall(text2))



# in default mode, it can not recognize \n
# you can use follow


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2)



'''
	In this pattern  (?:.|\n) specifies a noncapture group
	 (i.e., it defines a group for the purposes of matching, but that group is not captured separately or numbered).
'''


'or you can use a flag = re.DOTALL'

comment = re.compile(r'/\*(.*?)\*/', flags= re.DOTALL)
print comment.findall(text2)