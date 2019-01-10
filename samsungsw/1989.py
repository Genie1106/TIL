T=int(input())
word=[]
for i in range(T):
    word.append(input())

for w in word:
    print(w)
    for i in range(len(w)//2):
        if w[i]==w[len(w)-1-i]:
            result=1
        else:
            result=0
            break  
    print(f"#{word.index(w)+1} {result}")        