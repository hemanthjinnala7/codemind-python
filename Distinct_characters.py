a=input()
b=list(a)
c=[]
for i in b:
    if i not in c:
        c.append(i)
d=str(c)
e=[]
for i in d:
    if i.isalnum() and i.islower():
        e.append(i)
print(''.join(sorted(e)))



