A,B=map(int,input().split())
case_A=list(map(int,input().split()))
case_B=list(map(int,input().split()))

print(case_A)
# for b in range(B-A+1):
#     case_A[]
a = [1,2,3]
b = [3,4,5,6]

if len(case_A) > len(case_B) :
    case_A,case_B = case_B,case_A
max_result = 0
n = len(case_B)
for i in range(n) :
    result = 0
    if i + len(case_A) < n :
        for j in range(len(case_A)) :
            result += case_A[j]*case_B[i+j]
            print(case_A[j],case_B[i+j])
        if max_result < result :
            max_result = result
print(max_result)

