
from konlpy.tag import Okt
t = Okt()
import re
import gensim
from gensim.models import word2vec
import pandas as pd
import pymongo

client = pymongo.MongoClient('mongodb://dss:dss@'ip':27017')
db = client['melon_chart']
collection = db.song_list
df = pd.DataFrame(list(collection.find()))
df.drop(columns=['_id'], inplace=True)

# 가사 전처리: 한글, 영어, 숫자만 남기고 모든 특수문자 제거
def cleanse(text):
    pattern = re.compile(r'\s+')
    text = re.sub(pattern, ' ', text)
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', text)
    return text

# 기간, 연관 단어 입력 하여 유사한 음악 추첯
def search_similarity(year_end, year_start, look_keyword):
    yrange = df[(df['Year'] < year_end) & (df['Year'] >= year_start)].reset_index(drop=True)
    lyrics = yrange['Lyrics'].apply(cleanse)
    lyrics = lyrics.tolist()
        
    results = []
    for i in lyrics:
        result = t.pos(i, norm=True, stem=True)
        
        word = []
        for a in result:
            if not a[1] in ["Josa", "Determiner", "Exclamation", "Suffix"]:
                word.append(a[0])
        words = (" ".join(word)).strip()
        results.append(words)
        
    data_file = 'lyrics.data'
    with open(data_file, 'w', encoding='utf-8') as fp:
        fp.write("\n".join(results))
    data = word2vec.LineSentence(data_file)
    model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
    model.save('lyrics.model')
    model = word2vec.Word2Vec.load("lyrics.model")
    song = model.wv.most_similar(look_keyword, topn=10)
    keyword = []
    for s in song:
        keyword.append(s[0])
    relist = yrange[yrange['Lyrics'].str.contains('|'.join(keyword))]
    
    return relist.sample(n=10)
