C = int(input())
rate = []

for i in range(0,C):
    score = map(int,input().split())
    a = list(score)
    length = len(a) - 1
    New = sum(a) - a[0]
    avg = float(New/length)

    count = 0
    for i in range(1,length+1):
        if (a[i]) > avg:
            count= count+1
        else:
            count = count        
    rate.append("%0.3f" % float((count/length)*100))

for i in range(0,C):
    print(f"{rate[i]}%")