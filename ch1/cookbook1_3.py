'1.3 Keeping the Last N Items'

'Problem: want to keep a limited history of the last few items '

from collections import deque

'deque(maxlen=history) to set its volume'
'beside ordinary lists, it provies special methods: popleft() appendleft() (double-side access'


def search(lines, patterns, history=5):
	previouse_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previouse_lines
		previouse_lines.append(line)

# Example use on a file

# if __name__ == '__main__':
# 	with open('somefile.txt') as f:
# 		for line, previouse_lines in search(f, 'python',  5):
# 			for pline in previouse_lines:
# 				print(pline, end='')
# 			print(line)
# 			print('-'*28)

'If new to Generators, see Chapter 4 --'

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print q
q.appendleft(-1)
q.appendleft(-2)
print q
print q.pop()
print q
print q.popleft()
print q