n=int(input())
sqr=n**2
add=0
while sqr:
    r=sqr%10
    add=add+r
    sqr=sqr//10
if (add==n):print("Neon Number")
else: print("Not Neon Number")
    