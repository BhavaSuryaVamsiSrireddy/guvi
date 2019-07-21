n = list(input())
a = []
for i in n:
	a.append(int(i))
s = str(sum(a))
if(s == s[::-1]):
	print('YES')
else:
	print('NO')
