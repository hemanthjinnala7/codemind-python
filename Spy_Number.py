n=int(input())
q=0
s=1
while n:
    r=n%10
    q=q+r
    s=s*r
    n=n//10
if q==s: print("Spy Number")
else:
    print("Not Spy Number")
    