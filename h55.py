n,d = map(int,input().split())
l = list(map(str,input().split()))
c = 0
i = 0
while(c < d):
	a = l[i]
	l.remove(a)
	l.append(a)
	c = c + 1
print(' '.join(l))
