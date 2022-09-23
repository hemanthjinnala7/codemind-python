n=int(input())
arr = list(map(int,input().split()))
s=0
for i in arr:
    s+=i
if s%2==0:
    print("1")
else:
    print("0")