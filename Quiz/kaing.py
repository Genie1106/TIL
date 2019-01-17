def limit(a,b):
    new=0
    if a>b:
        new=a
    else:
        new=b
    while new:
        if new%a==0 and new%b==0:
            return new
        new+=1
           
M,N,X,Y=map(int,input().split())
x=0
y=0
cnt=0
cnt_x=0
cnt_y=0
for t in range(limit(M,N)):
    if X==x and Y==y:
        print(cnt)
        break
    x+=1
    y+=1
    cnt+=1
    
    if x>M:
        x=1
        cnt_x+=1
    if y>N:
        y=1
        cnt_y+=1

    if cnt_x>M:
        print("-1")
        break

if cnt==limit(M,N):
    print("-1")
    