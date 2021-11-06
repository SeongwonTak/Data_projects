# wanted_jd
# Want to do : 특정 키워드에 대해서 JD를 crawling, 및 직접 링크를 타고 들어가서 JD를 수집해와서 저장한다.
# 어떻게 데이터를 저장할 것인지에 대한 연구 포함.
# 그냥 bs4로는 되지 않는다... 클릭을 해야 한다.
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def crawler():
    # 시도1). wanted에서 '데이터 사이언티스트로 나오는 항목을 검색한다'
    # requested = requests.get("https://www.wanted.co.kr/wdlist/518/1024?country=all&job_sort=company0000000000.response_rate_order&years=-1")
    # html = requested.text
    # soup = BeautifulSoup(html, "html.parser")
    # 대체 각 블럭을 어떻게 가져오는건지.
    # 각 블럭의 URL을 가져오려고 한다.
    # data = soup.select_one('#__next > div > div._1yHloYOs_bDD0E-s121Oaa > div._2y4sIVmvSrf6Iy63okz9Qh > div > ul')
    # print(data)

    # 불가능.! 'disabled'로 뜨는걸 봐서는 동적 크롤링을 하지 않는 이상 어려워보인다.

    # 시도2) wanted의 URL구조는 wanted.co.kr/wd/숫자 구조이다.
    # requested = requests.get('https://www.wanted.co.kr/wd/1009')
    # html = requested.text
    # soup = BeautifulSoup(html, 'html.parser')
    # data = soup.select_one('#__next > div > div._37L2cip40tqu3zm3KC4dAa > div._17tolBMfrAeoPmo6I9pA1P > div._1FVm15xN253istI2zLF_Ax > div > div._31EtVNPZ-KwYCXvVZ3927g > section > p:nth-child(1) > span:nth-child(1)')
    # 동일한 방법으로 시도했으나, data가 얻이지지 않은 것으로 보아 다른 시도를 해야 하는 것으로 보인다....
    # print(data)

    pass


if __name__ == '__main__':
    crawler()