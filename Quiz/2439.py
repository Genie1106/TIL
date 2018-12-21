n = int(input())

for i in range(1,n+1):
    star = '*' * i
    blank = " "
    print(star.rjust(n,blank))

