def find(new_map,N,x):
    result=0
    for i in range(N):
        word=""
        for n in range(N):
            word+=str(new_map[i][n])
        word=word.split("0")
        result+=word.count("1"*x)
    return result

def change(change_map,N):
    copy_map=[[0]*N for n in range(N)]
    for n in range(N):
        for m in range(N):
            copy_map[n][m]=change_map[m][n]
    return copy_map
        
T=int(input())
test_result=[]

for i in range(T):
    N,x=map(int,input().split())
    mapping=[]

    for a in range(N):
        mapping.append(list(map(int,input().split())))

    test_result.append(find(mapping,N,x)+find(change(mapping,N),N,x))

for i in range(T):        
    print(f"#{i+1} {test_result[i]}")