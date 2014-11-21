'Json'

'JSON (JavaScript Object Notation).'

import json
from pprint import pprint
data = {
    "name":"wangchao",
    "height":173,
    "weigh":62,
    "diploma":"banchelor"
}

json_str = json.dumps(data)

he_data = json.loads(json_str)
pprint(he_data)

# Wriiting Json data

with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)



"""

The format of JSON encoding is almost identical to Python syntax except for a few minor changes. For instance, True is mapped to true, False is mapped to false, and None is mapped to null.
"""


d = {
    'a': True,
    'b': 'Hello',
    'c': None
}
print(json.dumps(False))
print(json.dumps(True))
print(json.dumps(None))
print(json.dumps(d))



