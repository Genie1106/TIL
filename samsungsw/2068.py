# 0개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

T = int(input())
case = []

for i in range(T):
    case.append(list(map(int,input().split())))

for i in range(T):
    high = 0
    for n in range(0,10):
        if case[i][n]>=high:
            high = case[i][n]
    print(f"#{i+1} {high}")