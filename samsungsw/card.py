T=int(input())
for t in range(T):
    N=int(input())
    num=input()
    high=0
    for i in num:
        if num.count(i)>high:
            high=num.count(i)
            alot=i
        elif num.count(i)==high:
            if i>alot:
                alot=i
    print(f"#{t+1} {alot} {high}")
