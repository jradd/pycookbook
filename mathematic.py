

'1.find prime'
'use filter'
a= (filter(lambda x: len(filter(lambda y: x%y==0, range(2, x-1)) ) ==0, list(range(2,101))  ))
for x in a:
    print(x)
# filter(lambda x: len(
#        filter(lambda y: x%y == 0,range(2,x-1))) == 0 , range(2,101) )
# ))

def f(x):
    if x%2==0:return True
print(list(filter(f, [1,23,3,4])))



'set calculation'
print(set(range(2,100)) - set([x for x in range(2,100) for y in range(2,x) if x % y == 0]))