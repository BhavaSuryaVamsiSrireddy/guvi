try:
    n=input()
    n=n.split()
    s=n[0]
    k=int(n[1])
    a=s[0:k]
    b=s[k:]
    b=b+a
    print(b)
except:
    print('invalid')
