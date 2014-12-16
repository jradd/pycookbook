'1.8 Calculating with Dictionaries'

"""
Problem

You want to perform various calculations (e.g., minimum value, maximum value, sorting, etc.) on a dictionary of data.
"""

prices = {
	'ACME': 45,
	'APPL':432,
	'IBM':40,
	'GOGL':37
}


# do calculating with  (value, key) pairs

min_prices = min(zip(prices.values(), prices.keys()))
max_prices = max(zip(prices.values(), prices.keys()))
print("min prices's stock is {0}".format(min_prices))
print("max prices's stock is {0}".format(max_prices))

# similiarly you can sort data.

prices_sorted = sorted(zip(prices.values(), prices.keys()), key=lambda x:x[0])
print(prices_sorted)
#>> [(37, 'GOGL'), (40, 'IBM'), (45, 'ACME'), (432, 'APPL')]