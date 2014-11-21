'1.12 Determining the Most Frequently Occurring Items in a Sequence'

"""
Problem

You have a sequence of items, and you’d like to determine the most frequently occurring items in the sequence.
"""
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)

print(top_three)

# Counter = a dict of word - frequency
print(word_counts)

# special methods:
# most_common, subtract?   update
# print dir(word_counts)


morewords = ['why','are','you','not','looking','in','my','eyes']

word_counts.update(morewords)
print(word_counts)

