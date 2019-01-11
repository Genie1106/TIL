T=int(input())
Test=[]

for R in range(T):
    New_wrod=""
    N,S=map(str,input().split())
    for i in S:
        New_wrod+=i*int(N)
    Test.append(New_wrod)

for i in Test:
    print(i)