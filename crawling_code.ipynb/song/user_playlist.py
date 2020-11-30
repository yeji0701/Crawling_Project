
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def playlist(seq):

        url = "https://www.melon.com/mymusic/playlist/mymusicplaylistview_listSong.htm?plylstSeq={}".format(seq)
        headers = {
            "User-Agent" : UserAgent().chrome
        }
        response = requests.get(url, headers=headers)
        dom = BeautifulSoup(response.text, 'html.parser')
        elements = dom.select("#frm > div > table > tbody tr")
        
        datas = []
        for element in elements:
            data = {
                "Title" : element.select_one("a.fc_gray").text,
                "Artist" : element.select_one("#artistName").text.replace('\n', ''),
                "Link" : 'https://www.melon.com/song/detail.htm?songId=' + element.select_one('td > div > input').get('value')
                }
            datas.append(data)
    
        return pd.DataFrame(datas)
