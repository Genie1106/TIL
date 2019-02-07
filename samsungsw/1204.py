T=int(input())
for t in range(T):
    a=int(input())
    Num=list(map(int,input().split()))
    high,many=0,0
    for i in Num:
        if i!=many:
            if Num.count(i)>high:
                high=Num.count(i)
                many=i
            elif Num.count(i)==high:
                if i>many:
                    many=i
    print(f"#{a} {many}")