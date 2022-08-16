a=input()
b=list(a)
c=[]
for i in b:
    if i not in c:
        c.append(i)
b=str(c)
r=[]
for i in b:
    if i.isalnum()==True and i.islower()==True:
        
        r.append(i)
print(len(r))

