def change(origin,case,result):
    new_test_case=[[]*1 for n in range(N)]
    for n in range(N):
        for m in range(N):
            new_test_case[n].append(case[N-m-1][n])
        result[n].append("".join(map(str,new_test_case[n])))    
    if origin == new_test_case:
        return result
    change(origin,new_test_case,result)

T=int(input())
for t in range(T):
    N=int(input())
    test_case=[]
    result=[[]*N for N in range(N)]
    for i in range(N):
        test_case.append(list(map(int,input().split())))
    change(test_case,test_case,result)
    print(f"#{t+1}")
    for n in range(N):
        for m in range(3):
            print(result[n][m],end=" ")
        print("")