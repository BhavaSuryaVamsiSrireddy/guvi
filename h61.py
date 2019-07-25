n = int(input())
l = list(map(int,input().split()))
u,v = map(int,input().split())
ui = []
vi = []
il = []
for i in range(len(l)):
	if l[i] == u:
		ui.append(i)
for i in range(len(l)):
	if l[i] == v:
		vi.append(i)
for i in ui:
	for j in vi:
		s = i - j
		il.append(abs(s))
print(min(il))
