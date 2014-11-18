'1.13 Sorting a List of Dict by common key'

'''
Problem

You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values.
'''
'Think about its a small db, sort by one column'


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
    {'fname': 'Dig', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key= itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows, key= itemgetter('uid'))
print(rows_by_fname)

print("\nsort by multiple keys")
rows_by_uid_fname= sorted(rows, key=itemgetter('uid','fname'))
print(rows_by_uid_fname)
# The itemgetter() can also accept multiple keys



'also i will use lambda function '
print("\nsort by keys, lambda")
new = sorted(rows, key = lambda x: x['fname'])
print(new)
'also i will use lambda function more keys'

print("\nsort by multiplekeys, lambda")
new = sorted(rows, key = lambda x: (x['fname'], x['uid']) )
print(new)