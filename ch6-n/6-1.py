'ch 6 - renew'


' csv io'


import csv

# 'testdata =   ./test.csv'


with open('d:/datadict.csv', encoding='utf-8') as f:
    f_csv = csv.DictReader(f)
    i = 1
    for row in f_csv:
        i += 1
        print(i, )
        print(row['SYSTEM_TYPE'])
        print(row['REMARK'])


# '_ use DictReader of csv'
# with open('test.csv') as f:
#     f_d_csv = csv.DictReader(f)
#     for row in f_d_csv:
#         print(row)



# 'some special header'
# header = 'Street Address,Num-Premises,Latitude,Longitude'
# import re
# print(re.sub('[^a-zA-Z_]', ',', header))
