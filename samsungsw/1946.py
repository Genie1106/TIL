T=int(input())
for t in range(T):
    string=[]
    N=int(input())
    for i in range(N):
        alp,num = map(str,input().split())
        string.append(alp*int(num))
    new_string="".join(string)
    cir=len(new_string)//10 +1
    print(f"#{t+1}") 
    for i in range(cir):
        print(new_string[10*i:10*i+10])



