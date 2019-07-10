
r = []
n = input()
s = list(n)
ns = list(set(s)) #removing duplicates using set and type-casting it to list.
l = len(ns)
for i in range(len(s)):
	if(l>0):# when distinct elements list length is not equal to zero it enters the loop.
		if n[i] in ns:
			r.append(s[i])
			ns.remove(s[i]) #removing distinct in list whenever it encountered.
			l = l - 1
		else:
			r.append(s[i])
	else:# when distinct elements list length becomes zero it comes out of the loop.
		break
print(len(r))
			
