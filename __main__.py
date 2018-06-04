import collection
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as et
from itertools import count

import time
from selenium import webdriver
from datetime import datetime

RESULT_DIRECTORY = '__result__/crawling'

# Goobne collection
def crawling_goobne():
    url = 'http://www.goobne.co.kr/store/search_store.jsp'
    wd = webdriver.Chrome('C:\cafe24\python\webdriver/chromedriver.exe')
    wd.get(url)
    time.sleep(3)

    results = []

    for page in count(start=1):
    # 테스팅
    #for page in range(101, 104):
        script = 'store.getList(%d)' % page
        wd.execute_script(script)

        print('%s : success for script execution {%s}' % (datetime.now(), script))
        time.sleep(3)

        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser')

        tag_tbody = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            #print(strings)

            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    for t in results:
        print(t)

    # store
    for t in results:
        print(t)

    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])

    print(table['sido'], table['sido'])
    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))
    #
    table = table.reset_index().set_index('index')
    table.to_csv('{0}/table-goobne.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
        # print(tags_tr)

# pelicana collection
def crawling_pelicana():
    results = []
    # range하고 끝을 지정안해주면 무한 루프.
    for page in count(start=1):#range(1, 6):
        url =f'http://pelicana.co.kr/store/stroe_search.html?page={page}&branch_name=&gu=&si='
        print(url)
        html = collection.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class':'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            # print(strings)

            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]
            # print(sidogu)

            results.append((name, address) + tuple(sidogu))

    # store
    for t in results:
        print(t)

    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])

    print(table['sido'], table['sido'])
    table['sido'] = table.sido.apply(lambda v: collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))
    #
    table = table.reset_index().set_index('index')
    table.to_csv('{0}/table-pelicana.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)

def proc_nene(xml):
    results = []
    root = et.fromstring(xml)
    items = root.findall('item')

    for item in items:
        name = item.findtext('aname1')
        sido = item.findtext('aname2')
        gungu = item.findtext('aname3')
        address = item.findtext('aname4')

        results.append((name, address, sido, gungu))

    return results

def store_nene(data):
    # 지금 pansas에러... 버전땜시 그런듯?
    # 데이터 프레임 만드는 작업.
    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])

    print(table['sido'], table['sido'])
    table['sido'] = table.sido.apply(lambda v:  collection.sido_dict.get(v, v))
    table['gungu'] = table.sido.apply(lambda v: collection.gungu_dict.get(v, v))
    #
    table = table.reset_index().set_index('index')
    table.to_csv('{0}/table-nene.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    #
    # print(table)

if __name__ == '__main__':
    # pelicana collection
    # crawling_pelicana()
    crawling_goobne()

    # nene collection
    # 한글이 저렇게 뜨는 경우는 문자열의 특징을 이용한다.
    # collection.crawling(
    #     url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
    #         % (urllib.parse.quote('전체'), urllib.parse.quote('전체')),
    #     proc=proc_nene,
    #     store=store_nene
    # )
    pass
