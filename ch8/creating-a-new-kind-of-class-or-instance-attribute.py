'Creating a New-Kind of Class or Instance Attribute'

'You want to create a new kind of instance attribute type with some extra functionality, such as type checking.'

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not instance(value,int):
            raise TypeError('expect an int')
        instance.__dict__[self.name] = value

    def __delete__(self, isinstance):
        del instance.__dict__[self.name]