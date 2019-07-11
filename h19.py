i,j = map(int,input().split())
l = []
for k in range(i):
    l.append(input().split())
m = l[0]
le = len(m)
for k in range(1,len(l)):
    n = 0
    while(n<le):
        if(m[n] in l[k]):
            n = n+1
        else:
            m.remove(m[n])
            le = le - 1
print(' '.join(m))      
