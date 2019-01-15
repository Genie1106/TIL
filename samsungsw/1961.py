def change(origin,case,result):
    new_test_case=[[]*1 for n in range(N)]

    for n in range(N):
        for m in range(N):
            new_test_case[n].append(case[N-m-1][n])
        print(new_test_case)
        # result[m][n].append("".join(map(str,new_test_case[i])))

    # for i in range(N):
    #     for
    #     print("".join(map(str,new_test_case[i])))

    if origin == new_test_case:
        return print("the end")
    else:
        change(origin,new_test_case,result)

N=int(input())
test_case=[]
result=[[]*N for N in range(N)]
print(result)
for i in range(N):
    test_case.append(list(map(int,input().split())))
change(test_case,test_case,result)