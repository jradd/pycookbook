

' Captureing variables in anonymous functions'

x = 10
a = lambda y : x+y

x = 20
b = lambda y: x+y

print(a(100))

print(b(200))

# 在調用此函數是 發現有個 全局變量 x  要在全局變量中找到最新的x的值. 因此 x= 20 被找到, 並且替代了 原有的x= 10 . 儘管他離 a lambda 函數更近.


'Making an N-Argument Callable Work As a Callable with Fewer Arguments '


def spam(a, b, c, d):
    print(a,b,c,d)


from functools import partial
s1 = partial(spam, 1)  # a = 1
s1(200,300,400)
s2 = partial(spam, d= 10.0)
s2(200,300,400)



'Replacing Single Method Classes with Functions'


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2,3), callback=print_result)
apply_async(add, ('hello','world'), callback=print_result)

class ResultHandler:
    def __init__(self):
        self.sequence= 0
    def handler(self, result):
        self.sequence+= 1
        print('[{}] Got: {}'.format(self.sequence, result))
r = ResultHandler()
apply_async(add, (2,3), callback=r.handler)
apply_async(add, ('hello','world'), callback=r.handler)


# == wait 你這本書之前不是說要 用函數 替代 只有一個函數的類 嗎??  別急 現在來替代.


def make_handler():
    sequence = 0
    def hander(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return hander

handler = make_handler()
apply_async(add, (2,3), callback=handler)
apply_async(add, ('hello','world'), callback=handler)




' inlining callback functions '

from queue import Queue
from functools import wraps

class Async:
    def __init__(self, fucn, args):
        self.func= func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Quene()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try :
                a= f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put )
            except StopIteration:
                break
        return wrapper


def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

test()