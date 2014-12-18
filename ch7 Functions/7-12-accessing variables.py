
def sample():
    n = 123123123
    # Closure Function
    def func():
        print('n=', n)

    # Acessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
print(dir(f))  # 'get_n', 'set_n' inside

print(f)
print(f.get_n)

# A1
'There are two main features that make this recipe work. First, nonlocal declarations make it possible to write functions that change inner variables'

'Second, function attributes allow the accessor methods to be attached to the closure function in a straightforward manner where they work a lot like instance methods (even though no class is involved).'


import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # updating instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items() if callable(value))
    def __len__(self):
        return self.__dict__['__len__']()

# example use

def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()

# show it actually works

s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('hello')

print(len(s)); print(s)

print(s.pop())


# old way

class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

'comment: Interestingly, this code runs a bit faster than using a normal class definition.'