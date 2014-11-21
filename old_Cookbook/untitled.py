from collections import namedtuple

#print(dir(namedtuple))

import re


header = "Street Address,Num-Premises,Latitude,Longitude"

headers = re.sub('[^a-zA-Z_]', '_', header)
print(headers)