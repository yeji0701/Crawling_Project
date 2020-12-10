
import pandas as pd
import pymongo
import math
import numpy as np
import random
import song.user.user_playlist as playlist

# mongodb에 연결해서 dataframe 만들기 : 전체곡 정보 데이터프레임 : df
client = pymongo.MongoClient('mongodb://dss:dss@'ip':27017')
db = client['melon_chart']
collection = db.song_list
df = pd.DataFrame(list(collection.find()))
df.drop(columns=['_id'], inplace=True)


# 장르선호도가 유사한 연도 ranking top5 뽑는 함수
def top5_list(seq, df=df):
    # NEW DATAFRAME
    recommend = []
    recommend_df = pd.DataFrame()
    
    # 1. 전체인기곡들 장르유사도
    df = df[df["Year"] >= 1980].reset_index(drop = True)
    # MAKE YEAR-RANGE
    ## elements 
    bins = round((np.max(df["Year"]) - np.min(df["Year"]))/4)
    labels = []
    for i in (range(np.min(df["Year"]) , np.max(df["Year"]) +1,4)):
        labels.append(str(i) + '-' + str(i+3))
    # DIVIDED BY 4YR-CYCLE
    ## ex) 1980-1983 , ... ,2016-2019
    df['year_range'] = pd.cut(x=df['Year'], bins= bins ,labels=labels)
    df["count"] = 1
    df_pivot = pd.pivot_table(data = df , values = "count", index = "Year", columns = "Genre",aggfunc = np.sum)
    df_pivot.fillna(0, inplace = True)
    df_normal = round(df_pivot.div(df_pivot.sum(axis = 1), axis=0),3)
    df_normal = df_normal.reset_index()
    
    # 2. 유저플레이리스트 장르유사도  함수
    df_user = playlist.user(seq)
    df_user.reset_index()
    # PIVOT
    df_user["count"] = 1
    user_pivot = pd.pivot_table(data = df_user, values = "count", columns="Genre",  aggfunc = np.sum)
    user_pivot.fillna(0, inplace=True)
    # 특정장르곡수/전체장르곡수 나눈 값 df : 사용자플레이리스트의 장르유사도 df
    user_normal = round(user_pivot.div(user_pivot.sum(axis=1), axis=0), 3)
    user_normal = pd.DataFrame(user_normal, columns=['R&B/Soul', '국내영화/국내드라마', '그외', '댄스','랩/힙합','록/메탈','발라드','성인가요','인디음악','재즈','포크/블루스'])
    np.nan_to_num(user_normal, copy=False)

    # 3. 장르유사도 비교 : 전체인기곡들 & 유저플레이리스트
    # 오차 구하기
    for i in range(len(df_normal)):
        error = (df_normal.loc[i] - user_normal) ** 2
        error = error.sum(axis =1)
        error = np.sqrt(error)
        recommend.append(error)
        
    # rms 칼럼만 만들기, 컬럼명 count를 rms로 변경
    from pandas import DataFrame
    recommend_df = pd.DataFrame(recommend)
    recommend_df.rename(columns={"count":"rms"}, inplace=True)
    
    # recommend_df 에 Year 값 넣은 df 만들기, df_normal에서 Year 컬럼 선택
    year = pd.DataFrame(df_normal["Year"])
    
    # Year 컬럼있는 df와 rms 컬럼있는 df 합치기
    recom = pd.concat([year,recommend_df], axis=1, join="inner")
    
    # 유사도 상위5개 : 인덱스 수정하기 위해 .reset_index(drop=True)
    ranking = recom.sort_values(by="rms", ascending=True).reset_index(drop=True)
    
    # 상위 5개 뽑기
    top5_r = pd.DataFrame()
    for i in range(0, 5):
        top5 = df[df["Year"] == ranking["Year"][i]]
        top5_r = pd.concat([top5_r, top5])

    fir = df[df["Year"] == ranking["Year"][0]] 
    sec = df[df["Year"] == ranking["Year"][1]]
    thr = df[df["Year"] == ranking["Year"][2]]
    four = df[df["Year"] == ranking["Year"][3]]
    fif = df[df["Year"] == ranking["Year"][4]]
    
    # 상위 5개 연도에서 가중치부여해서 random 곡 뽑기
    first = fir.take(np.random.permutation(len(fir))[:10])
    second = sec.take(np.random.permutation(len(fir))[:8])
    third = thr.take(np.random.permutation(len(fir))[:6])
    fourth = four.take(np.random.permutation(len(fir))[:4])
    fifth = fif.take(np.random.permutation(len(fir))[:2])
    
    # 뽑은 곡들 합해서 새로운 playlist 만들기
    result = pd.concat([first, second, third, fourth, fifth])
    
    return result
