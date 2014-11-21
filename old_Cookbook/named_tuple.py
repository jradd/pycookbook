from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(11, y = 22)
p2 = Point(x = 3, y =4)
print(p1)
print(p2)
print(type(p1))
#>><class '__main__.Point'>