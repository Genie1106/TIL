T=int(input())
for t in range(T):
    P,Q,R,S,W=map(int,input().split())
    A = P*W
    if W<=R:
        B=Q
    else:
        B=Q+S*(W-R)
    print(f"#{t+1} {min(A,B)}")