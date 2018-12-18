lunch = {'만둣국':'054-461-1838','육개장':'054-472-8863','낙지돌솥비빔밥':'054-483-9999'}

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items(): # list [(key, value)]
        csv_writer.writerow(item)
        # f.write(f'{item[0]},{item[1]}\n')
        

