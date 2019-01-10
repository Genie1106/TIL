T=int(input())
N=[]
for i in range(T):
    N.append(int(input()))

for i in N:
    print(f"#{N.index(i)+1}",end=" ")
    tri = [[1]*i for i in range(1,i+1)]

    for n in range(1,i):
        for m in range(1,i):
            if n<=m:
                break
            else:
                tri[n][m]=tri[n-1][m-1]+tri[n-1][m]
            
    for a in range(i):
        print()
        for b in range(len(tri[a])):
            print(tri[a][b],end=" ")
    print(" ")