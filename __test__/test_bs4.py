# beautifulsoup4 test

from bs4 import BeautifulSoup

html = '<td class="title">'\
       '<div class="tit3" id="test">'\
       '<a href="/movie/bi/mi/basic.nhn?code=158178" title="독전">독전</a>'\
       '</div>'\
       '</td>'

# 1. 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))

    tag = bs.td
    print(tag, type(tag))
    # .태그이름으로 태그에 접근가능
    print(tag.div)

    # a herf 태그만
    tag = bs.a
    print(tag, type(tag))
    print(tag.name)


# 2. Attribute 값
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    # td안에 있는 class 값을 가져옴
    print(tag['class'])

    tag = bs.div
    print(tag['id'])    # id가 없으면 에러
    print(tag.attrs)    # 속성값 통째로 dic형태


# 3. Attribute 조회
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    # 이걸 많이 사용함. (정교하게 가져올 수 있기 때문)
    # td태그 중 class가 title인 애만 가져오라ㅏ.
    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    # title이 독전이 애의 정보를 가져와라
    tag = bs.find(attrs={'title': '독전'})
    print(tag)

    # a태그를 가져와라
    tag = bs.find('a')
    print(tag)

if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()