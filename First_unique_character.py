a=input()
b=list(a)
c=[]
dis=0
for i in b:
    if b.count(i)==1:
        c.append(i)
        dis=1
d=str(c)
e=[]
for i in d:
    if i.isalnum()==True and i.islower()==True:
        e.append(i)
if dis==0:
    print("-1")
else:
    print(e[0])
