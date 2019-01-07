# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

T = int(input())
test = []

for i in range(T):
    test.append(input())

for i in range(T):
    month = int(test[i][4])*10+int(test[i][5])
    date = int(test[i][6])*10+int(test[i][7])
    print(month,date)
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if date>31:
            print("-1")
    elif month == 2:
        if date>28:
            print("-1")
    elif month == 4 or 6 or 9 or 11:
        if date>30:
            print("-1")
    else:
            print("-1")

    print(f"{test[i][0:4]}/{test[i][4:6]}/{test[i][6:8]}")