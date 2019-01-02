# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

A,B,C = map(int,input().split())

if A>=B:
    first = A
    second = B
else:
    first = B
    second = A

if second>=C:
    second = second
else:
    if first>=C:
        second = C
    else:
        second = first  
    
print(second)


