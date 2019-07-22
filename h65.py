n,k = map(str,input().split())
l = list(map(str,input().split()))
le = len(l)
i = 0
while(i<le):
	if l[i] == k:
		l.remove(l[i])
		le = le - 1
		i = i
		continue
	i = i + 1
if( len(l) == 0 ):
	print('empty')
else:
	print(' '.join(l))
