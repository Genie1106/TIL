T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    test_case=list(map(int,input().split()))
    result=[]

    for i in range(N-M+1):
        result.append(sum(test_case[i:i+M]))

    print(f"#{t+1} {max(result)-min(result)}")