T=int(input())

N,x=map(int,input().split())
grade=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
score=[]

for i in range(N):
    score.append(list(map(int,input().split())))

for i in range(N):
    score[i]=(score[i][0]*35)+(score[i][1]*45)+(score[i][2]*20)

total_score=sorted(score,reverse=1)
cutline = N//10
cnt = 0

for i in range(10):
    if total_score.index(score[x-1])<cutline:
        break
    else:
        cutline+=cutline
        cnt+=1
print(grade[cnt])       