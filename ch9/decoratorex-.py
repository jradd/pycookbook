from functools import wraps

def makebold(func):
    def wraps():
        result = func()
        return "<b>" + str(result) +"</b>"
    return wraps

def makeitalic(func):
    def wraps():
        result = func()
        return "<i>" + str(result) +"</i>"
    return wraps

@makebold
@makeitalic
def say():
   return "Hello"
# print(say())

def shout(word="yes"):
    return word.capitalize() + "!"


print(shout())

'既然函数是一个对象, 当然可以把一个对象赋值给另一个变量'
scream = shout

print(scream())

# 我能不能删除已经创建的 shout ??

del shout
print(scream())  # it still alive...


def talk():
    # define a function on the fly in 'talk'
    def whisper(word='yes'):
        return word.lower() + '...'

    print(whisper())

talk()
# if call whisper, you got an error, because whisper is not defined.


def getTalk(kind='shout'):
    #
    def shout(word='yes'):
        return word.capitalize()+'!'
    def whisper(word='yes'):
        return word.lower() + '...'

    if kind == 'shout':
        return shout
    else :
        return whisper

talk = getTalk()

print(talk)
print(talk('whisper'))
print(getTalk('whisper')())


def dosomethingbefore(func):
    print('I do something before')
    print(func())

dosomethingbefore(scream)

def my_shiny_new_decorator(a_function):
    def the_wrapper_around_the_original_function():
        print('>>>> before run ')
        a_function()
        print('>>>> after run')
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print('i am stand lovejj')

a_stand_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_decorated()
