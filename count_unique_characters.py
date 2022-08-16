a=input()
b=list(a)
c=[]
for i in b:
    if b.count(i)==1:
        c.append(i)
d=str(c)
e=[]

for i in d:
    if i.islower()==True:
        e.append(i)
print(len(e))
        


