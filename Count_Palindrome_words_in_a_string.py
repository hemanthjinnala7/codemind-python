a=list(map(str,input().split()))
b=0
c=[]
for i in range(len(a)):
    if a[i].upper() or a[i].islower():
        c.append(a[i].lower())
for i in range(len(c)):
    if c[i]==c[i][::-1]:
        b+=1
print(b)





