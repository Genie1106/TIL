T=int(input())
for t in range(T):
    A,B=map(int,input().split())
    case_A=list(map(int,input().split()))
    case_B=list(map(int,input().split()))
    if len(case_A)>len(case_B):
        new=case_A
        case_A=case_B
        case_B=new
    high=0
    for j in range(len(case_B)-len(case_A)+1):
        result=0
        for i in range(len(case_A)):
            result+=case_A[i]*case_B[j+i]
        if result>high:
            high=result
    print(f"#{t+1} {high}")