T=int(input())
grade=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
new_grade=[]

for a in range(T):
    score=[]
    N,x=map(int,input().split())
    for i in range(N):
        score.append(list(map(int,input().split())))

    for i in range(N):
        score[i]=(score[i][0]*35)+(score[i][1]*45)+(score[i][2]*20)

    total_score=sorted(score,reverse=1)
    cutline = N//10
    first_cutline=N//10
    cnt = 0

    for i in range(10):
        if total_score.index(score[x-1])<cutline:
            break
        else:
            cutline+=first_cutline
            cnt+=1        
    new_grade.append(grade[cnt]) 

for i in range(len(new_grade)):
    print(f"#{i+1} {new_grade[i]}") 