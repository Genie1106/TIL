T=int(input())

for t in range(T):
    N=int(input())
    test_case=list(map(int,input().split()))
    high,low=test_case[0],test_case[0]
    for i in test_case:
        if i>high:
            high=i
        if low>i:
            low=i
    print(low,high)        
    print(f"#{t+1} {high-low}")