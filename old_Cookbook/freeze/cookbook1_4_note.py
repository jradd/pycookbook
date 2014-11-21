'1.4 Finding Largest N items or Smallest N items '

import heapq, random

nums = [ random.randint(0,100) for i in range(10)]
print nums

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


'How about dealing with dicts'

'generate a stock name, from 4 random letters'

def ge4letter():
	return  reduce(lambda x,y : x+y, [chr(random.randint(67, 91))  for i in range(4) ] )

print ge4letter()
portfolio = []
for i in range(40):
	stockDict = {}
	stockDict['price'] = random.randint(10, 20)
	stockDict['share'] = random.randint(50, 100)
	stockDict['name'] = ge4letter()
	portfolio.append(stockDict)
# for k, v in stockDict.items():
	# print k, v
for stock in  portfolio : print stock

cheap = heapq.nsmallest(3, portfolio, key = lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key = lambda s : s['price'])

