num=[]
scale = map(int,input().split())
cnt = 0
for i in scale:
    num.append(i)

for i in range(1,len(num)):
    if abs(num[i-1] - num[i])==1:
        if num[i-1]>num[i]:
            cnt = 0
        else:
            cnt = 1
    else:
        cnt = 2
        break

if cnt==0:
    print("descending")
elif cnt==1:
    print("ascending")
else:
    print("mixed")        