a=int(input())
b=str(a)
c=0
for i in range(len(b)):
    c+=int(b[i])**(i+1)
if c==a:
    print("True")
else:
    print("False")

