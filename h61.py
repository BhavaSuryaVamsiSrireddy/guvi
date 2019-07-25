n = int(input())
l = list(map(int,input().split()))
u,v = map(int,input().split())
ui = []
vi = []
il = []
for i in l:
	if i == u:
		ui.append(l.index(i))
for i in l:
	if i == v:
		vi.append(l.index(i))
for i in ui:
	for j in vi:
		s = i - j
		il.append(abs(s))
print(min(il))
