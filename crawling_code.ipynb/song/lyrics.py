
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_lyrics(link):
    headers = {"User-Agent" : UserAgent().chrome}
    response = requests.get(link, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    elements = dom.select_one('.wrap_lyric').text.replace('\r', '').replace('\n', '').replace('\t', '').split('펼치기')[0]
    if elements == '[가사 준비중] 멜론 회원 여러분! 가사 등록을 기다리고 있어요.가사등록하기':
        elements = '-'
        
    return elements
