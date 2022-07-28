n=int(input())
add=0
while n>0 or add>=10:
    if n==0:
        n=add
        add=0
    r=n%10
    add+=r
    n=n//10

print(add)

    