T=int(input())

for t in range(T):
    sdoku=[]
    test=1
    
    for i in range(9):
        sdoku.append(list(map(int,input().split())))

    for n in range(9):
        if not sum(sdoku[n])==45:
            test=0
            break

    for n in range(9):
        test_score=0
        for m in range(9):
            test_score+=sdoku[m][n]
        if not test_score==45:
            test=0
            break

    for n in range(0,9,3):
        test_score2=0
        for m in range(0,9,3):
            test_score2=sum(sdoku[n][m:m+3])+sum(sdoku[n+1][m:m+3])+sum(sdoku[n+2][m:m+3])
            if not test_score2==45:
                test=0
                break

    print(f"#{t+1} {test}")


