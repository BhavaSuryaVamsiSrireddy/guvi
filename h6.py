from collections import defaultdict
n = int(input())
l = list(map(int,input().split()))
r = []
c = defaultdict(list)
for i in range(n):
	if(l.count(l[i])>1):
		c[l[i]].append(i)
if(len(c)>0):
	for i,j in c.items():
		j.remove(j[0])
		j.sort()
		r.append([j,i])
	r.sort()
	print(r[0][1])
else:
	print('unique')

	
