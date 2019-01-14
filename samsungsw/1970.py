# [예제]
# N이 32850일 경우,
# 50,000 원 : 0개
# 10,000 원 : 3개
# 5,000 원 : 0개
# 1,000 원 : 2개
# 500 원 : 1개
# 100 원 : 3개
# 50 원 : 1개
# 10 원 : 0개
T=int(input())

for t in range(T):
    N=int(input())
    coin=[0,0,0,0,0,0,0,0]

    if N//10000:
        if N//10000>=5:
            for i in range((N//10000)//5):
                coin[0]=(N//10000)//5
                coin[1]=N//10000-((N//10000)//5)*5
        else:
            coin[1]=N//10000
        N=N-10000*(N//10000)

    if N//1000:
        if N//1000>=5:
            coin[2]=1
            coin[3]=(N//1000)-5
        else:
            coin[3]=N//1000        
        N=N-1000*(N//1000)

    if N//100:
        if N//100>=5:
            coin[4]=1
            coin[5]=(N//100)-5
        else:
            coin[5]=N//100       
        N=N-100*(N//100)

    if N//10>=5:
        coin[6]=1
        coin[7]=(N//10)-5
    else:
        coin[7]=N//10 

    print(f"#{t+1}")
    for i in coin:
        print(coin,end=" ")
    print("")


    


