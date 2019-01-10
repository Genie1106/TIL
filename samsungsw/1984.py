T=int(input())
score=[]

for i in range(T):
    score.append(list(map(int,input().split())))

for i in score:
    high = max(i)
    low = min(i)
    i.remove(high)
    i.remove(low)
    avg= round((sum(i)/len(i)),1)
    print(f"#{score.index(i)+1} {avg}")