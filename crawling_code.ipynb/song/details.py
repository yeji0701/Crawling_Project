
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
    
        return datas
