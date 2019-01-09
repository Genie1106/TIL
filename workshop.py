N=int(input())
for i in range(0,N+1):
    if N <= i**2:
        a=i-1
        b=i
        break
while round(a,7)!=round(b,7):
    if ((a+b)/2)**2 > N:
        b=(a+b)/2
    else:
        a=(a+b)/2
print(round(a,6))