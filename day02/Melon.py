import requests
import bs4

response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select('div[class=tit3]')

https://ssl.pstatic.net/imgmovie/2007/img/common/bullet

with open("Movie.txt",'w',encoding='utf8') as f: # with open() as f:
    print("실시간 movie 순위\n")
    for rank in result:
        f.writelines(f'{rank.text}\n')
