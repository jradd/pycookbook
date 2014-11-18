'2.10 Working with Unicode Characters in Regex'

"""

Problem

You are using regular expressions to process text, but are concerned about the handling of Unicode characters.
"""


import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))


# Arabic digits

print(num.match('\u0661\u0662\u0663'))