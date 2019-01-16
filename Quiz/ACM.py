T=int(input())

for t in range(T):
    H, W, N = map(int,input().split())
    first=N%H
    second=N//H+1

    if first==0:
        first=H
        second-=1
        
    if second<10:
        second="0"+str(second)
    print(str(first)+str(second))
