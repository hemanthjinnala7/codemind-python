c=int(input())
for i in range(c):
    a=int(input())
    o=[]
    while a!=0:
        r=a%2
        o.append(r)
        a=a//2
    o.reverse()
    for ele in o:
        print(ele,end='')
    print()
    
  