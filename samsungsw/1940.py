T=int(input())
for t in range(T):
    N=int(input())
    status=[]
    vel=0
    distance=0
    for i in range(N):
        status.append(list(map(int,input().split())))
    for i in status:
        if i[0]==1:
            vel+=i[1]
        elif i[0]==2:
            vel-=i[1]
        if vel<0:
            vel=0
        distance+=vel
    print(f"#{t+1} {distance}")
