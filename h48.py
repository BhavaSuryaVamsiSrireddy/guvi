a = input()
b = input()
if b in a:
	for i in range((len(a)-len(b)+1)):
		if a[i:i+len(b)] == b:
			print(i)
			break
else:
	print(-1)
