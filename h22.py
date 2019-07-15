n = int(input())
l = list(map(int,input().split()))
p = []
for i in range(len(l)):
	m = 1
	for j in range(len(l)):
		if(i == j):
			continue
		else:
			m = m * l[j]
	p.append(str(m))
print(' '.join(p))
