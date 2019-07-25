n = int(input())
l = input().split()
p = input()
c = 0
for i in range(len(l)):
	if(len(l[i])>=len(p)):
		if(l[i][:len(p)] == p):
			c = c + 1
print(c)
