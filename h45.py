n = int(input())
l = list(map(int,input().split()))
r = []
for i in range(1,len(l)+1):
	m = i * n
	if m in l:
		r.append(l[i-1])
print(len(r))
