'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.

a = number % 2

if a == 0:
    print(f"{number}은 짝수이다\n")
else:
    print(f"{number}은 홀수이다\n")   


#number // 2 => number를 2로 나눴을 때의 몫
#number % 2 => number를 2로 나눴을 때의 나머지