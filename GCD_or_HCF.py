a,b=map(int,input().split())
mx=max(a,b)
c=[]
for i in range(1,mx+1):
    if a%i==0 and b%i==0:
        c.append(i)
print(max(c))