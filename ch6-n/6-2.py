'6-2 Json data'

'meaning: JSON (JavaScript Object Notation).'

import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23,
   'mmmm': None
}
json_pool = json.dumps(data)
data2 = json.loads(json_pool)
print(data2)


# writing jason data

with open('data.json','w') as f:
    json.dump(data2, f)


# reading from json file
with open('data.json', 'r') as f:
     data = json.load(f)








# use case

from urllib.request import urlopen
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))

from pprint import pprint
pprint(resp)


j = {
    "l1": {
        "l1_1": [
            "l1_1_1",
            "l1_1_2"
        ],
        "l1_2": {
            "l1_2_1": 121
        }
    },
    "l2": {
        "l2_1": None,
        "l2_2": True,
        "l2_3": {}
    }
}
