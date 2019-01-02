import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_k')

with open("NaverList.txt",'w',encoding='utf8') as f: # with open() as f:
    for rank in result:
        f.writelines(f'실시간 검색어 : {rank.text}\n')

