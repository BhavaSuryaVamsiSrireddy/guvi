try:
    s=int(input())
    n=input()
    n=n.split()
    l=[]
    for i in n:
        t=int(i)
        l.append(t)
    l=sorted(l)
    if(s%2==0):
        s=s//2
        m=(l[s]+l[s-1])//2
    else:
        s=s//2
        m=l[s]
    print(m)
except:
    print('invalid')
