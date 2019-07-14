n = int(input())
l = list(map(int,input().split()))
le = len(l)
while(le>0):
	if(le%2 == 0):
		m = le//2
		a = (l[m-1] + l[m])//2
		print(a)
		l.remove(l[m])
		l.remove(l[len(l)//2])
		le = le - 2
	else:
		m = le//2
		print(l[m])
		l.remove(l[m])
		le = le - 1
