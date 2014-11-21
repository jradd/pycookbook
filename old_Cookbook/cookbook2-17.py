# coding=utf-8
'2.17 Handling HTML and XML Entities in Text'


"""Proble


Problem

You want to replace HTML or XML entities such as &entity; or &#code; with their corresponding text. Alternatively, you need to produce text, but escape certain characters (e.g., <, >, or &).

"""

s = 'Elements are written as "<tag>text</tag>".'

import html

print s

# print html.escape(s)
# print html.escape(s, quote= False)


# s = 'Spicy Jalapeño'
# print s.encode('ascii', errors='xmlcharrefreplace')


'2.18 Tokenizing Text'

text = 'foo =23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import 	re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ,WS]))

'In these re patterns, the ?P<TOKENNAME> convention is used to assign a name to the pattern. '


scanner = master_pat.scanner('foo = 42')
print scanner.match()
print scanner.match().lastgroup()
#, _.group()