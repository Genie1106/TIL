T=int(input())
for t in range(T):
    K,N,M=map(int,input().split())
    bus_stop=list(map(int,input().split()))
    bus,cnt,i=0,0,0

    while K>0:
        if bus+K in bus_stop:
            bus=bus_stop[bus_stop.index(bus+K)]
            i=bus_stop.index(bus)+1
            cnt+=1
        elif bus+K > bus_stop[i]:
            for k in range(1,K):
                if bus+K-k == bus_stop[i]:
                    bus=bus+K-k
                    cnt+=1
                    i+=1
                    break
        else:
            cnt=0
            break

        if N-bus<=K:
            break
    print(f"#{t+1} {cnt}")


