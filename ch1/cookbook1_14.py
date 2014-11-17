'1.14 Sorting Objects without native Comparison support'

"""
Problem

You want to sort objects of the same class, but they don’t natively support comparison operations.


"""

class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(users)



from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

"""
The choice of whether or not to use lambda or attrgetter() may be one of personal preference. However, attrgetter() is often a tad bit faster and also has the added feature of allowing multiple fields to be extracted simultaneously.

suggest use attrgetter
"""