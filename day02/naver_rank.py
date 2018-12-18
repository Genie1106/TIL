import requests
import bs4

h= {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.melon.com/chart/index.htm',headers=h).text
print(response)

# soup = bs4.BeautifulSoup(response, 'html.parser')
# result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')

# with open("NaverRank.txt",'w',encoding='utf8') as f :
#     for item in result:
#         rank = item.select_one('.ah_r').text
#         name = item.select_one('.ah_k').text
#         f.writelines(f'실시간 {rank}위 - {name}\n')

# with open("NaverList.txt",'w',encoding='utf8') as f: # with open() as f:
#     for rank in result:
#         f.writelines(f'실시간 검색어 {}: {rank.text}\n')
