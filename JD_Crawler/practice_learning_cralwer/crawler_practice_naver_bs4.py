# Goal : Naver datalab에서 12일 정도의 검색어를 받아오기.
# 받아와서 일자, 1위 ~ 10위 총 12일치를 dataframe으로 만든다.
# DataFrame형태로 출력하면 목표 성공.
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def main():
    # 1단계. 기본적으로 request라는 것은 html문서를 가져오도록 요청하는 행위
    webpage = requests.get("https://datalab.naver.com/").content
    soup = BeautifulSoup(webpage, "html.parser")

    # 2단계. 태그를 확인 후 태그에 맞는 정보를 가져오기
    rank_item = []
    rank_date = []
    date_data = soup.select('.rank_title')  # 일자만 따온다.
    for item in date_data:
        rank_date.append(item.get_text())

    item_data = soup.select('.rank_list .title')  # 1 ~ 10위 순서대로 하루 일자, 각 일자별로 아이템 추출.
    for item in item_data:
        rank_item.append(item.get_text())

    # print(rank_date) -> 깔끔하게 나오지 않음
    # rank_data 전처리
    rank_date.pop()
    rank_date.pop()
    for i in range(len(rank_date)):
        rank_date[i] = rank_date[i][1:-1]

    # rank_item 전처리
    # 10개씩 12묶음이 되도록 정리한다.
    rank_item = np.array(rank_item).reshape((10, 12))

    # 최종 데이터 프레임 생성
    data_df = pd.DataFrame(rank_item, columns= rank_date, index = range(1, 11))
    print(data_df)

    # Problem : 해당 사이트에서 패션 탭은 정리했는데.. 다른 거는 정리 못할까?
    # 카테고리별로 다른 카테고리를 뽑고 싶다. 동적 크롤링에 대해 고려해봐야 할 것이다.

if __name__ == '__main__':
    main()

