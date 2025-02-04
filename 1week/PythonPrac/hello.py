from pprint import pprint

import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

pprint(rjson)

rows = rjson['RealtimeCityAir']['row']
pprint(rows)

for gu in rows:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']

    if gu_mise < 60:
        print(gu_name, gu_mise)