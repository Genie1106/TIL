T=int(input())
for t in range(T):
    color_map=[[0]*10 for i in range(10)]
    N=int(input())
    test_case=[]
    cnt=0
    for n in range(N):
        test_case.append(list(map(int,input().split())))

    for i in test_case:
        if i[4]==1:
            for m in range(i[0],i[2]+1):
                for n in range(i[1],i[3]+1):
                    color_map[m][n]=1
        else:
            for m in range(i[0],i[2]+1):
                for n in range(i[1],i[3]+1):
                    color_map[m][n]+=1
    
    for c in color_map:
        cnt+=c.count(2)
    print(f"#{t+1} {cnt}")

