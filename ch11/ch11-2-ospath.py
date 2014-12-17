'ch11.2 os.path'

import os

cwd = os.getcwd()
print(cwd) # E:\我的坚果云\Git\pythoncookbook\ch11
path = os.path('.')
print(os.path.abspath(path))
'''os.path.

        abspath

'''