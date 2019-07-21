n = list(input())
f = 0
for i in range(len(n)):
	a = n[i]
	n.remove(n[i])
	if(''.join(n) == ''.join(n[::-1])):
		f = 1
		break
	n.insert(i,a)
if(f == 1):
	print('YES')
else:
	print('NO')
	
