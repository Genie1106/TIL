N=int(input())
game=[3,6,9]

def clap(n,i):
    if n%10 in game or n//10 in game:
        if n%10 in game and n//10 in game:
            print("--",end=" ")
        else:
            print("-",end=" ")
    else:
        print(i,end=" ")

for i in range(1,N+1):
    if i//100:
        new=i-(i//100)*100
        if i//100 in game:
            if new%10 in game or new//10 in game:
                if new%10 in game and new//10 in game:
                    print("---",end=" ")
                else:
                    print("--",end=" ")
            else:
                print("-",end=" ")    
        else:
            clap(new,i)
    else:
        clap(i,i)