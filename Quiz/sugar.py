N=int(input())
a = int(N/5)
b = N%5

if b==0:
    print(a)
elif b==3:
    print(a+1)

else:
    if a>0:
        if b==1:
            print(a+1)
        elif b==4:
            print(a+2)
        else:
            if a>1:
                print(a+2)
            else:
                print("-1")        
    else:
        print("-1") 