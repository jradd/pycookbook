'2.7Specifying a Regular Expression for the Shortest Match'

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no." '
print(str_pat.findall(text1))

text1 = 'Computer says "no." '
text2 = 'Computer says "no." Phone says "yes". '
print(str_pat.findall(text2))
#>> ['no." Phone says "yes']
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
#>> ['no.', 'yes']

"This makes the matching nongreedy, and produces the shortest match instead."

