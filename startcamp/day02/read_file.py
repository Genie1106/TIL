
with open("ssafy.txt",'r',encoding='utf8') as f: # with open() as f:
    lines =  f.readlines()
    for line in lines:
        print(line.strip())