month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
T=int(input())
for t in range(T):
    A,B,C,D = map(int,input().split())
    date=1
    while A<C:
        date+=month.get(A)
        A+=1
    date=date+D-B
    print(f"#{t+1} {date}")