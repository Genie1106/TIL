'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요. 

price = prices.split(';') #특정 문자열에서 자를 때 : split()
print(price)

a=[] # 새로운 list를 만듦.
for i in price:
    n=int(i) #price가 문자열이므로 숫자열로 바꿔줘야 함.
    a.append(n) # a라는 list에 원소 추가. append : 리스트에 추가적으로 넣는다.
    
a.sort(reverse=True) #내림차순으로 정렬
print(a)

# 1. split() 이용 
# 2. 반복을 통한 item들 int() 이용
# 3. .sort() or sorted() 정렬
# 1. 출력
