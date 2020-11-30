
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def playlist_genre(link):
    headers = {"User-Agent" : UserAgent().chrome}
    response = requests.get(link, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    
    return dom.select_one('dd:nth-of-type(3)').text
