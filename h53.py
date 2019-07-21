a,b = map(str,input().split())
a = list(a)
b = int(b)
s = ''
for i in range(len(a)-b+1):
	s = s + ''.join(a[i:i+b]) + ' '
print(s)
