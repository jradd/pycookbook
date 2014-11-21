'2.15 Interpolating Variables in Strings'


s = '{name} has {n} messages.'

print s.format(name='Guido', n = 37)

name = 'Guido'
n = 37

# Python 3
# print s.format_map(vars())


class Info:
	def __init__(self, name, n):
		self.name = name
		self.n = n

# a = Info('Guido', 37)
# s.format_mat(vars(a))


# missing value , it may deal not gracefully


# s.format(name='Guido') # KeyError

