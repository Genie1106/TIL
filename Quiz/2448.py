
N = int(input())
blank = " "
star = "*"

half = int((N-1)/2)
print(half)
print(half*blank+star)
for i in range(1,):
    
    print((half-i)*blank + star + blank*(i+1) + star)

# print(i*blank+star)
# print((i-1)*blank+star+blank*1+star)
# print((i-2)*blank+star+blank*3+star)