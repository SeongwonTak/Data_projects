# 이번에는 top 100 게임에 대한 게임 정보를 가져오려고 한다.
# 이를 위해서는 다시 랭킹 페이지에서 url만 가져오고, 이를 바탕으로 스팀 페이지를 긁어보자.
# 가져오려는 것은 리뷰 개수와 게임 메인 태그, 출시 연도 정도다.
# 이를 바탕으로 추가 분석을 진행하려고 한다.

import pandas as pd
import numpy as np
import re
import requests
import bs4

page_nums = ['p.1', 'p.2', 'p.3', 'p.4']
url_based = 'https://steamcharts.com/top/'
link_list = []
game_list = []
count = 0
df = pd.DataFrame(columns = ['Game', 'top_5_tags', 'review_level', 'review_count'])

for page_num in page_nums:
    url = url_based + page_num
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    links = soup.find_all("td",{"class":"game-name left"})

# 우리에게 필요한건 a href에 들어간 사이트 주소와 게임 이름이다.

    for l in links:
        link = l.find('a')['href']
        game = l.get_text()

        link_list.append(link)
        game_list.append(game)


for i in range(0, 100):
    cur_game = link_list[i]
    tag = []

    # 스팀 페이지랑, 스팀 차트는 app number가 잘 공유되고 잇다.
    steam_based = 'https://store.steampowered.com'
    steam_url = steam_based + cur_game
    r = requests.get(steam_url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    tags = soup.find_all("a",{"class":"app_tag"})
    get_tag_len = min(5, len(tags))
    for t in tags[:get_tag_len]:
        cur_tag = t.get_text()
        cur_tag = cur_tag.replace('\n', "")
        cur_tag = cur_tag.replace('\t', "")
        cur_tag = cur_tag.replace('\r', "")
        tag.append(cur_tag)


    if soup.find("span",{"class":"game_review_summary positive"}):
        review_level = soup.find("span",{"class":"game_review_summary positive"}).get_text()
    elif soup.find("span", {"class": "game_review_summary mixed"}):
        review_level = soup.find("span",{"class":"game_review_summary mixed"}).get_text()
    elif soup.find("span", {"class": "game_review_summary "}):
        review_level = soup.find("span",{"class":"game_review_summary "}).get_text()
    else:
        review_level = 'cannot_find'

    if soup.find("span",{"class":"user_reviews_count"}):
        review_count = soup.find("span",{"class":"user_reviews_count"}).get_text()
    else:
        review_count = '0'

    review_count = review_count.replace('(',"")
    review_count = review_count.replace(')',"")
    review_count = review_count.replace(',',"")

    cur_game_name = game_list[i]
    cur_game_name = cur_game_name.replace('\n', "")
    cur_game_name = cur_game_name.replace('\t', "")


    df.loc[i] = [cur_game_name, tag, review_level, review_count]

print(df.head(5))
df.to_csv('top100_steam_game_info.csv')
