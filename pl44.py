try:
    n=input()
    n=n.split()
    s=n[0]
    k=int(n[1])
    a=s[-k:]
    b=s[0:-k]
    b=a+b
    print(b)
except:
    print('invalid')
