# print(9>>1)

def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

anyargs()
anyargs("3",4,5)
anyargs("3",4,5,base=2,test=34)

print(help(anyargs))
# None  help doc


# print(dir(anyargs))
def add(x, y):
    pass
print(anyargs.__annotations__) # None
print(add.__annotations__) # None

# def add(x: int, y: int) -> int:
#     return x + y

# print(add.__annotations__)
# {'y': <class 'int'>, 'x': <class 'int'>, 'return': <class 'int'>}


'default arguments'
def spam(a, b=42):
    print(a,b)

# print(dir(spam))

def spam(a, b= []):
    a += 1
    b.append(4242)
    print(a, b)
print(spam.__defaults__)  # the default arguments list.

spam(1) ; print('spam(1) has')
print(spam.__defaults__)  # the default arguments list.

spam(3) ; print('spam(1) spam(3) has')
print(spam.__defaults__)  # the default arguments list.


## to avoid this use like this.

def spam(a, b=None):
    if not b:      # NO! Use 'b is None' instead
        b = []
    pass #...




