a=int(input())
b=int(input())
c=0
d=0
for i in range(1,a):
    if a%i==0:
        c+=i
for i in range(1,b):
    if b%i==0:
        d+=i
if a==d and b==c: print("Amicable")
else: print("Not Amicable")