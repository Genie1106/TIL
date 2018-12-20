# 도시별 최근 3일의 온도
city = {
    '서울' : [-6,-10,6],
    '대전' : [-3,-6,2],
    '광주' : [-0,-2,10],
    '구미' : [2,-2,9],
}

#3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''

for i in city.keys():
    
    count = len(city[i])
    temp = 0

    for t in range(0,count):
        temp = temp + city[i][t]
        avg = round (temp / count,2)
        
    print(f"{i} : {avg}º")  
    