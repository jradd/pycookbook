'4.5 Iterating in Reverse'


print dir([1,2])

# there is a   __reversed__ method

class Countdown:
	def __init__(self, start):
		self.start = start

	# Forward iterator
	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n
			n += 1


c = Countdown(10)
for num in reversed(c): print num
