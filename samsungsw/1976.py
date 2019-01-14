# [제약 사항]
# 시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
# 첫 번째 수가 시를 나타내고 두 번째 수가 분을 나타낸다. 그 다음 같은 형식으로 두 번째 시각이 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 시를 출력하고 공백을 한 칸 둔 다음 분을 출력한다.
T=int(input())

for i in range(T):
    Test_case=list(map(int,input().split()))

    hour=Test_case[0]+Test_case[2]
    minute=Test_case[1]+Test_case[3]

    if minute>=60:
        hour+=1
        minute-=60

    if hour>12:
        hour-=12

    print(f"{i+1} {hour,minute}")

