'ch 6 - renew'


' csv io'


import csv

'testdata =   ./test.csv'


'normal csv reader'
with open('test.csv') as f:
    f_csv = csv.reader(f)
    header = next(f_csv) # delimiter is ',' can change.
    print(header); print(type(header))
    for row in f_csv:
        pass# print(row)


'_ use DictReader of csv'
with open('test.csv') as f:
    f_d_csv = csv.DictReader(f)
    for row in f_d_csv:
        print(row)



'some special header'
header = 'Street Address,Num-Premises,Latitude,Longitude'
import re
print(re.sub('[^a-zA-Z_]', ',', header))
