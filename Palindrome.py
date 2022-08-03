a=input()
i=0
j=len(a)-1
flag=True
while (i<j):
    if a[i]!=a[j]:
        flag=False
    i=i+1
    j=j-1
if (flag==True): print("True")
else: print("False")