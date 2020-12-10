
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

def song_details(year):
    url = "https://www.melon.com/chart/age/list.htm?idx=1&chartType=YE&chartGenre=KPOP&chartDate={}&moved=Y".format(year)
    headers = {
        "User-Agent" : UserAgent().chrome
    }
    response = requests.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    elements = dom.select("#frm > table > tbody tr")
    
    datas = []
    for element in elements:
        data = {
            "Title" : element.select_one('a > .odd_span').text.split('상')[0].strip(),
            "Artist" : element.select_one('div > .fc_mgray').text,
            "Year" : year,
            "Link" : 'https://www.melon.com/song/detail.htm?songId=' + element.select_one('td > div > input').get('value')
        }
        datas.append(data)
    df = pd.DataFrame(datas)
    
    return df

#상세 페이지 내 장르 수집 함수
def get_genre(link):
    headers = {"User-Agent" : UserAgent().chrome}
    response = requests.get(link, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    
    return dom.select_one('dd:nth-of-type(3)').text

#상세 페이지 내 가사 수집 함수
def get_lyrics(link):
    headers = {"User-Agent" : UserAgent().chrome}
    response = requests.get(link, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    elements = dom.select_one('.wrap_lyric').text.replace('\r', '').replace('\n', '').replace('\t', '').split('펼치기')[0]
    if elements == '[가사 준비중] 멜론 회원 여러분! 가사 등록을 기다리고 있어요.가사등록하기':
        elements = '-'
        
    return elements

def run(year):
    df = song_details(year)
    df['Genre'] = df['Link'].apply(get_genre)
    df['Lyrics'] = df['Link'].apply(get_lyrics)
    df.drop(columns=['Link'], inplace=True)
    
    return df
