import random
sc=0
def puzzle(l,sc):
    le1=len(l)-1
    i1=random.randint(0,le1)
    k=list(l[i1])
    le2=len(k)-1
    ri=[]
    for i in range(2):
        rig=random.randint(0,le2)
        if rig not in ri:
            ri.append(rig)
    for i in range(len(k)):
        if i in ri:
            k[i]='*'
    print(''.join(k))
    ans=input()
    if ans in l:
        print('right \n')
        sc=sc+1
        return sc
    else:
        print('wrong \n')
        print('answer is '+l[i1])
        print('\nyour score is '+str(sc))
        sc=-1
        return sc
print('WORD PUZZLE GAME')
print('''1.fruits
2.vegetables
3.countries''')
c=input('Enter your choice:')
while(sc>=0):
    fruits=['apple','banana','pineapple','grapes','orange']
    vegetables=['potato','peas','tomato','brinjal']
    countries=['india','china','japan','korea']
    if(c=='1'):
    	sc=puzzle(fruits,sc)
    elif(c=='2'):
    	sc=puzzle(vegetables,sc)
    elif(c=='3'):
    	sc=puzzle(countries,sc)
    else:
    	print('invalid choice')
    	break

