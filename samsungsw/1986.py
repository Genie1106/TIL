T=int(input())
N=[] 
for i in range(T):
    N.append(int(input()))

for i in N:
    score=0
    for a in range(i+1):
        if a%2:
            score=score+a
        else:
            score=score-a
    print(f"#{N.index(i)+1} {score}")