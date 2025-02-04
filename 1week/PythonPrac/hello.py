from pprint import pprint

import requests # requests 라이브러리 설치 필요

def get_gu_mise(name):
    r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
    rjson = r.json()

    pprint(rjson)

    rows = rjson['RealtimeCityAir']['row']
    pprint(rows)

    for gu in rows:
        gu_name = gu['MSRSTE_NM']
        gu_mise = gu['IDEX_MVL']
        if gu_name == name:
            return gu_mise
    return "미세먼지 수치가 없습니다."

print(get_gu_mise("중구"))
print(get_gu_mise("종로규"))
print(get_gu_mise("수지구"))