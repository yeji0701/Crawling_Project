
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_genre(link):
    headers = {"User-Agent" : UserAgent().chrome}
    response = requests.get(link, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    
    return dom.select_one('div.entry > div.meta > dl > dd:nth-child(6)').text
