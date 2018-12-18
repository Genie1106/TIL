with open("싸피.txt",'r',encoding='utf8') as f:
    lines = f.readlines() 
    l = reversed(lines)
    #reversed()
    #lines.reverse
    
    with open("ssafy_reverse.txt",'w',encoding='utf8') as n:
        for line in l:
            n.write(line)
            print(line)
