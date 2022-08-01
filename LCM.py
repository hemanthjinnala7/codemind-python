a,b=map(int,input().split())
mx=max(a,b)
mn=min(a,b)
gcd=0
for i in range(1,mn+1):
    if a%i==0 and b%i==0:
        gcd=i
lcm=abs(a*b)//gcd
print(lcm)
        