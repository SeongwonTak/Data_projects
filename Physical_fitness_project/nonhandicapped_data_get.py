# 공공기관 API를 받아서 data를 받아오고 정리하는 방법에 대해 정리한다.
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15004104
# 사용자 데이터가 존재하는 29934명을 모두 가져온다.
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
def main():
    print("[START]")
    encoding = '{blind}'
    # request url정의
    # 29934의 값은 현재 구할 수 있는 데이터 전체 개수이다.
    url = "http://www.kspo.or.kr/openapi/service/nfaTestInfoService/getNfaTestRsltList?serviceKey=" + encoding\
          + "&pageNo=1&numOfRows=29934"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "lxml")

    items = soup.find_all("item")
    print(len(items))
    columns = items[0].find_all()
    col_length = len(columns)

    col_namelist = []
    for i in range(0, col_length):
        col_namelist.append(columns[i].name)

    # 전략 : DataFrame을 만들어버린다.
    df = pd.DataFrame(columns = col_namelist)
    # 여기에 하나씩 추가하는 방식으로 하면 된다. 간단하게  df.loc[i] = [...] 이런식으로 하면 된다.
    # 즉 한줄씩 value를 따와야 한다. 아주 간단하게.
    for i in range(0, len(items)):
        cur_val = []
        cur_item = items[i].find_all()
        add_idx = 0
        for j in range(0, col_length):
            # 만일 이번에 보는 줄에 해당 태그가 존재할 경우
            # 해당 태그에 들어간 값을 추가하고 다음 볼 태그로 넘긴다.
            # 일부 줄에서 결측치 처리 대신에 값이 아예 안들어간 경우가 존재하여 어쩔 수 없다.
            # 전처리 단계에서 보완한다.
            if col_namelist[j] == cur_item[add_idx].name:
                cur_val.append(cur_item[add_idx].text)
                add_idx += 1
            else:
                cur_val.append(np.nan)
        df.loc[i] = cur_val

    df.to_csv('non_handi.csv')
    print('[end]')

if __name__ == '__main__':
    main()
