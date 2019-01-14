def test(new_sdoku):
    for i in range(9):
        for n in range(9):
            if not num[n] in sdoku[i]:
                return 0    

def mkmatrix(origin_sdoku):
    column = []
    for n in range(9):
        for m in range(9): 
            column[n].append(origin_sdoku[m][n])
    print(column)

sdoku=[]
num=[1,2,3,4,5,6,7,8,9]

for i in range(9):
    sdoku.append(list(map(int,input().split())))

print(test(sdoku)) #가로 검사.
print(sdoku[0][0])
mkmatrix(sdoku)

# 세로

# # 3x3

# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9