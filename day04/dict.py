# 1. 딕셔너리 만들기
lunch = {
    '중국집' : '02-123-1234',
    '양식집' : '054-478-9985',
    '한식집' : '054-485-2223'
}

dinner = dict(중국집 = '02-123-1234')

# 2. 딕셔너리에 내용 추가하기
lunch['분식집'] = '054-463-5556'

# 3. 딕셔너리 내용 가져오기
print(lunch["중국집"]) ## 결과값 : 중국집의 전화번호 출력

idol = {
    'BTS' : {
        '지민':24,
        'RM' : 25
    }
}

print(idol['BTS']) #{'지민': 24, 'RM': 25}으로 결과값이 나옴
print(idol['BTS']['RM']) # RM의 25가 출력.


# 4. 딕셔너리 반복문 활용하기
# 기본할용
for key in lunch:
    print(key) # key
    print(lunch[key]) #Value

# key만 가져오기 : .keys() : list처럼 사용 가능/
for key in lunch.keys():
    print(f'Key : {key}')    


# Value만 가져오기 : .values() : list처럼 사용 가능/
for value in lunch.values():
    print(f'Value : {value}')   

#item(key,value) 가져오기 : .items()
#lunch.items() => [('중식집','02-123-1234), ...]
for lunch in lunch.items():
    print(lunch)


# 2개 = 자료형(list, tuple, ...) 길이2
a,b,c=(1,2,3)
print(a)
print(b)