n = int(input())
l = list(map(int,input().split()))
c = []
for i in range(len(l)):
	for j in range(i+1,len(l)+1):
		s = sum(l[i:j])
		c.append(s)
		s = 0
for i in l:
	c.append(i)
c.sort()
print(c[-1])
