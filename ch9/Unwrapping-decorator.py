'9.4 Unwrapping a Decorator'

' 去裝飾化'



import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def printmoreandmore(i):
    while i > 0:
        print(i, end=' ')
        i -= 1
    if i < 1:
        print()

printmoreandmore(5)
orig_printmore = printmoreandmore.__wrapped__
orig_printmore(5)




'multiple decorators 儘量不要用此方式'
'不知道去掉哪個 decorator...'
'Python3.3 是要去掉所有的'


'現在我們在3.4中試試會怎樣'

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x,y):
    return x + y


add(1, 2)


# 關於多裝飾器問題, 未來會有變化 也不一定.
# However, this behavior has been reported as a bug (see http://bugs.python.org/issue17482) and may be changed to explose the proper decorator chain in a future release.



