score = {
    '수학' : 80,
    '국어' : 90,
    '음악' : 100
}

# 이 학생의 평균을 구하라.
total = 0

for grade in score.values():
    total = total + grade

avg = total / len(score)
print(avg)

#  # 추가 풀이

total_score = sum(score.values()) #sum([80,90,100])=270
avg_score = total_score/len(score)
print(avg_score)

# 반 평균을 구라하라
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
    }
}

total_score = 0
cnt = 0

for i in scores.keys():
    i = scores[i].values()
    
    for student in i:
        total_score = total_score + student
        cnt+=1 # cnt++은 없음.

avg = total_score / cnt  
print(avg)

## 강사님 풀이.
total_score = 0
count = 0

for person_score in scores.values():
    person_score.values() 
     # person_score => [{'수학': 80, '국어': 90, '음악': 100}, {'수학': 70, '국어': 90, '음악': 100}]
     # person_score.values() => {'수학': 80, '국어': 90, '음악': 100}
     for subject_score in person_score.values():
         total_score += subject_score
         count +=1
        
avg_score = total_score / count
