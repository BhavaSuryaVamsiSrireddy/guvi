n = input()
a = []
d = []
for i in range(len(n)):
	if(n[i].isalpha()):
		a.append(n[i])
		continue
	if(n[i].isdigit()):
		d.append(int(n[i]))
		continue
s = ''
for i in range(len(d)):
	if(d[i]%2 == 0):
		for j in range(d[i]):
			s = s + a[i]
	else:
		s = s + a[i] + str(d[i])
print(s)
	
