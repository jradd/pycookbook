'1.11 Naming a Slice'
"""
Problem

Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up.


"""
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'

SHARES = slice(20,32)
PRICE = slice(40,48)
a=(record[SHARES])
b=(record[PRICE])
cost =(int(a)*float(b))
print(cost) # 51325.0

# set slice with steps (increment.)
a = slice(10, 50, 2)
b = slice(2, 50, 2)


