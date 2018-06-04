from urllib.request import Request, urlopen
from datetime import datetime
import sys

# None일 경우를 구분하기 위해서
# if문보다 훨씬 깔끔하다.
def proc(html):
    return html

def store(src):
    return src

def crawling(
        url='',
        encoding='utf-8',
        # proc=lambda html:html # 람다로 사용할 경우
        proc=proc,
        store=store,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)
        ):
    try:
        request = Request(url)
        resp = urlopen(request)

        # 인코딩 에러 날 경우 대비.
        # 'replace'는 알아서 대처해줌.
        try:
            receive = resp.read()
            result = receive.decode(encoding)
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        print('%s : success for request [%s]' % (datetime.now(), url))

        return store(proc(result))
    except Exception as e:
        err(e)