from itertools import permutations
n = input()
l = []
for i in n:
	l.append(i)
p = list(permutations(l))
for i in p:
	print(''.join(i))
