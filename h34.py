from itertools import permutations
n = list(input())
p = list(permutations(n))
p.sort()
id = p.index(tuple(n))
le = len(p)
if(id == le-1):
	print('impossible')
else:
	print(''.join(p[id+1]))
