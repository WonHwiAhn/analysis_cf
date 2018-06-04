from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

resp = urlopen(request)
html = resp.read().decode('cp949')

# print(html)

bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify())

# 일단 공통 속성을 이용해서 가져오고 최종 목표를 가져오는게 좋음.
tags = bs.findAll('div', attrs={'class': 'tit3'})
print(tags)

#for tag in tags:
#    print(tag.a.text)

for index, tag in enumerate(tags):
    print(index, tag.a.text, tag.a['href'], sep=': ')