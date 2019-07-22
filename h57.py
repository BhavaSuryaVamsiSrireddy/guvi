s = int(input())
n = list(map(int,input().split()))
for i in n:
	if n.count(i) == 1 :
		print(i)
		break
