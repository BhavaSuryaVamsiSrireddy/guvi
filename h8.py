# your code goes here
n = int(input())
m = list(map(int,input().split()))
for i in range(len(m)):
	a = m[i]
	for j in range(i+1,len(m)):
		b = m[j]
		s = a+b
		for k in range(j+1,len(m)):
			c = m[k]
			if(c == s):
				print(a,' ',b,' ',c)
		
