n = int(input())
l = list(map(int,input().split()))
r = []
for i in range(len(l)-1):
	if(l[i]>l[i+1]):
		r.append(str(l[i+1]))
	else:
		r.append('-1')
r.append('-1')
print(' '.join(r))
