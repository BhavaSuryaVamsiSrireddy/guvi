n = int(input())
l = list(map(int,input().split()))
r = []
for i in l:
	m = i * n
	if m in l:
		r.append(str(i))
if(len(r) > 0):
	print(' '.join(r))
else:
	print(0)
	
