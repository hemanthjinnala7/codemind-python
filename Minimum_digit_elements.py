a=int(input())
b=list(map(int,input().split()))
d=[]
e=0
count=0
for i in range(0,len(b)):
    c=str(abs(b[i]))
    d.append(len(c))
e=min(d)
for j in range(len(d)):
    if e==d[j]:
        count+=1
print(count)
    
   