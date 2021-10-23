# wanted_jd
# Want to do : 특정 키워드에 대해서 JD를 crawling, 및 직접 링크를 타고 들어가서 JD를 수집해와서 저장한다.
# 어떻게 데이터를 저장할 것인지에 대한 연구 포함.
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def main():
    # 1단계. wanted에서 '데이터 분석'이라고 검색한 페이지에 대해서 크롤링을 실시해본다.
    webpage = requests.get("https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D").content
    soup = BeautifulSoup(webpage, "html.parser")
    print(soup.find_all('header'))

if __name__ == '__main__':
    main()