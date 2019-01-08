# [제약 사항]
# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

T=int(input())
case=[]

for i in range(T):
    case.append(input())

for i in range(T):
    for a in range(1,30):
        if case[i][0]==case[i][a]:
            if case[i][0:a]==case[i][a:a+a]:
                print(f"#{i+1} {a}")
                break


