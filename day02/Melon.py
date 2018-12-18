import requests
import bs4

response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div.class="tit3"')

with open("Movie.txt",'w',encoding='utf8') as f: # with open() as f:
    for rank in result:
        f.writelines(f'실시간 movie : {rank.text}\n')
