'Creating Managed Attributes'

# 想做什麼 - 偉值對類型的檢查.

'You want to add extra processing (e.g., type checking or validation) to the getting or setting of an instance attribute.'

# 偉值.  所以應在 setter 過程中檢查.

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter
    @property
    def first_name(self):
        return sefl._first_name

    # Setter
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can not delete attribute')

