n = int(input())
l = list(map(int,input().split()))
p = []
rp = []
for i in range(len(l)):
	for j in range(i+1,len(l)+1):
		p.append(l[i:j])
for i in p:
	m = 1
	for j in range(len(i)):
		m = m * i[j]
	rp.append(m)
rp.sort()
print(rp[-1])
