T=int(input())
for t in range(T):
    sdoku=[]
    for i in range(9):
        sdoku.append(list(map(int,input().split())))    
    test=0    
    for n in range(9):
        if sum(sdoku[n])==45:
            print(test)
            test_score=0
            test_score2=0
            for m in range(9):
                test_score+=sdoku[m][n]
            print(test_score)
            if test_score==45:
                for a in range(0,9,3):
                    for b in range(0,9,3):
                        test_score2=sum(sdoku[a][b:b+3])+sum(sdoku[a+1][b:b+3])+sum(sdoku[a+2][b:b+3])
                        if test_score2==45:
                            test=1
            else:
                break
        else:
            break
    print(test)
    if test==1:                        
        print(f"#{t+1} 1")
    else:
        print(f"#{t+1} 0")