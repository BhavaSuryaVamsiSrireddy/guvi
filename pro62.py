# your code goes here
s = input()
ml = 1
start = 0
low = 0
high = 0
r = 0
l = len(s)
for i in range(1,l):
	low = i-1
	high = i
	while low >= 0 and high < l and s[low] == s[high] :
		if high - low + 1 > ml:
			start = low
			ml = high - low + 1
		low -= 1
		high += 1
	low = i - 1
	high = i + 1
	while low >= 0 and high < l and s[low] == s[high]:
		if high - low + 1 > ml:
			start = low
			ml = high - low + 1
		low -= 1
		high += 1
r =len(s) - len(s[start:start+ml])
print(r)
