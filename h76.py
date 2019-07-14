n = int(input())
m = []
for i in range(n):
	m.append(sum(list(map(int,input().split()))))
s = sum(m)
a = s/(n*n)
print('{0:.6f}'.format(a))
