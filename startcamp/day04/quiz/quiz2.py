scores = {
    'a' : {
        '수학' : 80,
        '국어' : 90,
        '음악' : 100
    },
    'b' : {
        '수학' : 70,
        '국어' : 90,
        '음악' : 100
    },
    'c' : {
        '수학' : 60,
        '국어' : 40,
        '음악' : 80
    },
    'd' : {
        '수학' : 90,
        '국어' : 50,
        '음악' : 20
    },

}

total_math = 0
total_korea = 0
total_music = 0
cnt = 0

for i in scores.keys():
    math = scores[i]['수학']
    total_math = total_math + math
    korea = scores[i]['국어']
    total_korea = total_korea + korea
    music = scores[i]['음악']
    total_music = total_music + music
    cnt+=1

avg_math = total_math / cnt
avg_korea = total_korea / cnt
avg_music = total_music / cnt

print(f"수학 평균 = {avg_math}")
print(f"국어 평균 = {avg_korea}")
print(f"음악 평균 = {avg_music}")
#     for student in i:
#         total_score = total_score + student

#         cnt+=1 # cnt++은 없음.

# avg = total_score / cnt  
# print(avg)
