# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

N,k = map(int,input().split())

array=[]
count=0
result=[]

for i in range(N):
    array.append(list(map(int,input().split())))

print(array[0][2:6]==[1,1,1])    
if array[0][2:6]==[1,1,1]:
    print("yes")
else:
    print("no")

for n in range(N):
    
    while array[n][]


# for n in range(N):
#     for m in range(N):
#         count=0
#         if array[n][m]==1:
#             if m+k<=N:
#                 if sum(array[n][m:m+k+1])==k:
#                     count+=1
#     result.append(count)

# if array[i].count(1)>=3:
    #     print("yes")
    #     array[i] = array[i].split(0)
    #     print(array)
    # else:
    #     print("no")

print(result)

