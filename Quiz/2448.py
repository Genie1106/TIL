
N = int(input())
blank = " "
star = "*"

half = int((N-1)/2)

print(half*blank+star)

for i in range(1,half+1):
    a = half - i
    b = int(N-2-(half/2-1)*2)
    print(a*blank + star + blank*b + star)

# print(i*blank+star)
# print((i-1)*blank+star+blank*1+star)
# print((i-2)*blank+star+blank*3+star)