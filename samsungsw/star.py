# T=int(input())
# score=[]
# for i in range(T):
#     N=int(input())
#     score.append(list(map(int,input().split())))

def maximun(n):
    high=0
    score=0
    for i in range(len(n[1])):
        if n[1][i]>high:
            high=n[1][i]
            high_line= i 
    
    for i in range(high_line):
        dif=high-n[1][i]
        score=score+dif

    print(high,score)
    
n=[[3, 5, 9], [1, 1, 4, 1, 2, 4]]

maximun(n)
