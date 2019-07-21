a,b = map(str,input().split())
a = list(a)
b = int(b)
s = []
for i in range(len(a)-b+1):
	s.append(''.join(a[i:i+b]))
print(' '.join(s))
