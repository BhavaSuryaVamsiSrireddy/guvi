r,col = map(int,input().split())
m = []
c = []
for i in range(r):
	m.append(list(map(int,input().split())))
for i in m:
	if 0 in i:
		for j in range(len(i)):
			if(i[j] == 0):
				c.append(j)
			i[j] = 0
for i in m:
	for j in c:
		i[j] = 0
for i in m:
	for j in range(len(i)):
		i[j] = str(i[j])
for i in m:
	print(' '.join(i))
		
