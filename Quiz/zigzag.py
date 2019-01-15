N=int(input())
plus=0

for i in range(1,N+1):
    plus+=i
    if plus>=N:
        point=i
        diff=N+i-plus
        break

if not point%2:
    a=diff
    b=point+1-diff
else:
    a=point+1-diff
    b=diff

print(f"{a}/{b}")