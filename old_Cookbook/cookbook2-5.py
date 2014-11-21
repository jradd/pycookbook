'2.5 Matching and Searching for Text Patterns'

"""Problem

You want to match or search text for a specific pattern.
"""

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

#'Today is 2012-11-27. PyCon starts 2013-3-13.'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print  datepat.sub(r'\3-\1-\2', text)


from calendar import month_abbr
print [ month_abbr[i] for i in range(1,13)]

def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print datepat.sub(change_date, text)