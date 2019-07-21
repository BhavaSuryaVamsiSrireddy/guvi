n = int(input())
l = list(map(int,input().split()))
d = {}
for i in range(len(l)):
	d[l[i]] = i
r = []
while(True):
	for i in range(len(l)):
		if((i+1)%2 == 0):
			r.append(l[i])
	if(len(r) == 1):
		break
	l = []
	l = r
	r = []
print(d[r[0]])
	
