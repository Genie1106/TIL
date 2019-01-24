T=int(input())
for test in range(T):
    N=input()
    num=[]
    t=1
    while len(num)<10:
        new_N=str(int(N)*t)
        for i in new_N:
            if not i in num:
                num.append(i)
        t+=1
    print(f"{test+1} {new_N}")
