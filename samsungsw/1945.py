Num=[2,3,5,7,11]
T=int(input())
for t in range(T):
    N=int(input())
    result=[0,0,0,0,0]
    i=0
    while N!=1:
        if not N%Num[i]:
            N=N//Num[i]
            result[i]+=1
        i+=1
        if i==5:
            i=0
    print(f"#{t+1}",end=" ")
    for i in result:
        print(i,end=" ")
    print(" ")