n = input()
l = list(n)
l.append('@')
r = []
res = []
s = ''
for i in range(len(l)):
	if  l[i] != ' ' and l[i] != '@':
		s = s + l[i]
		continue
	r.append(s)
	s = ''
le = len(r)
for i in r:
	if i != '':
		res.append(i)
print(' '.join(res))
