N=list(input())
num=["0","1","2","3","4","5","6","7","8","9"]
high=0

for t in range(len(N)):
    if N[t]=="9" or N[t]=="6":
        N[t]=N[t].replace("9","").replace("6","")

for i in num:
    if N.count(i)>1:
        cnt=N.count(i)
    else:
        cnt=1
    if cnt>high:
        high=cnt

if N.count(""):
    if N.count("")%2:
        new_cnt=N.count("")//2+1
    else:
        new_cnt=N.count("")//2

    if new_cnt>high:
        high=new_cnt

print(high)


