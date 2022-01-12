# steamcharts.com/top을 create할 것이다.
# link를 담아서 게임 번호를 입력 후, 해당 창을 가져오려고 한다.
# 해당 창에서 표에 있는 월간 유저수, 피크수 등을 모두 가져오려고 한다.
# 랭킹 페이지 : https://steamcharts.com/top/p.1 형태로 p.1,2,3,4 형태로 증가한다.

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
df = pd.DataFrame(columns = ['Game', 'Month', 'Avg_Players', 'Peak_Players'])

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

game_url_based = 'https://steamcharts.com/'

for i in range(len(link_list)):
    month = []
    avg_player = []
    peak_player = []
    game_url = game_url_based + link_list[i][1:]

    r = requests.get(game_url)
    soup_game = bs4.BeautifulSoup(r.text, 'lxml')
    months = soup_game.find_all("td",{"class":"month-cell left"})
    avg_players = soup_game.find_all("td",{"class":"right num-f"})
    peak_players = soup_game.find_all("td",{"class":"right num"})

    for m in months:
        cur_month = m.get_text()
        month.append(cur_month)

    for avg in avg_players:
        cur_avg = avg.get_text()
        avg_player.append(cur_avg)

    for peak in peak_players:
        cur_peak = peak.get_text()
        peak_player.append(cur_peak)

    for j in range(len(month)):
        df.loc[count] = [game_list[i], month[j], avg_player[j], peak_player[j]]
        count += 1

print(df.head(10))
df.to_csv('steam_game_data.csv')

