import random

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}



# 난이도* 1. 지역(location)은 몇개 있나요? : list length

location_num = len((ssafy['location']))
print(f'지역은 총 {location_num} 곳이 있습니다.')


# 난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in

for i in ssafy.keys():
    if i != 'requests':
        none = 0
    else:
        none = 1    
if none == 0:
    print("False")


# # 난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근

number1 = ssafy['classes']['gm']['class president']
print(f'gm반의 반장 : {number1}')


# # 난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복

for i in ssafy.keys():
    if i == 'language':
        study_language = ssafy[i].keys()

        for a in study_language:
            print(f"우리가 배우는 언어 : {a}")
        break    


# # 난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복

person = ssafy['classes']['gj']

for i in person.values():
    if(i=="change"):
        print(f"gj반의 강사 : {i}")
    elif(i=="pro-gj"):
        print(f"gj반의 매니저 : {i}")
       

# # 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation

people = ssafy['language']['python']['frameworks']

for i in people.items():
    if(i[0]=="flask"):
        print(f"flask는 {i[1]}이다.")
    elif(i[0]=="django"):
        print(f"django는 {i[1]}이다.")


# # 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.

group = ssafy['classes']['gm']['groups']['4조']
clean = random.choice(group)
print(f"오늘의 당번 : {clean}")

# print(f"오늘의 당번은 {name}")
# 출력예시)
# 오늘의 당번은 하창언
# '''