a,d=map(int,input().split())
count=0
b=list(map(int,input().split()))
for i in range(len(b)):
    c=str(abs(b[i]))
    if len(c)==d:
        count+=1 
print(count)