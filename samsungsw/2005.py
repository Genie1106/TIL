N,x=map(int,input().split())

test=[[1, 3, 3, 6, 7],[8, 13, 9, 12, 8],[4, 16, 11, 12, 6],[2, 4 ,1 ,23, 2],[9, 13, 4, 7, 3]]


# for i in range(N):
#     test.append(list(map(int,input().split())))

death=0
fly = 0
for n in range(N-1):
    for m in range(N-1):
        for i in range(n,n+x):
            fly = fly + sum(test[i][m:m+x-1])
            if fly>death:
                death=fly
print(death)
