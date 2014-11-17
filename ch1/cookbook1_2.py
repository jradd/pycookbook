'1.2 Unpacking Elements from Iterables of Arbitrary Length'

'Solution :  star expressions'
def avg(list):
	return sum(list)/len(list)

def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

print(drop_first_last([1,2,3,4]) )
print(drop_first_last([1,2,3]) )


'Attention, because use first, *middle, last, so the len(grades) must be greater than 2.'




user_record = ('Dave', 'dave@example.com', '773-55-1212','1234-32123-12')
name, email, *phone_numbers = user_record
print(phone_numbers)

items = [1,10,7,4,6,9]
head, *tail = items
print(tail)
