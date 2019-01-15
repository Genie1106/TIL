# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.

T=int(input())
test=[]

for t in range(T):
    N=int(input())
    test.append(list(map(int,input().split())))
    test[t].sort()
    new_test=" ".join(map(str,test[t]))
    print(f"#{t+1} {new_test}")

