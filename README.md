Crawling + Flask Project

Gathering music data and buiding recommendation system
======================================================
This project started off from a question: "Past fashion trend came back as 'newtro (new + retro)', so can music trend come back too?" 
The primary purpose was to crawl music data in the years 1960s~20100s from a music chart to explore and visualize. During this process, came an idea for a music recommendation system to answer another question: "What kind of modern music will a person with a playlist from the past listen to?"

The major activities in this project:
* Crawling data from 'Melon' chart
* Cleansing and exploring the gathered data
* Building algorithm for music recommendation
* Coding Flask and HTML to put algorithm in action

Prerequisites:
* Jupyter Notebook
* VS Code
* Python3

Getting Started
---------------
##### Packages to install
1. Crawling Melon chart:
* reqests
* BeautifulSoup (bs4)
* UserAgent (fake_useragent)
* pandas
2. Visualization:
* matplotlib.pyplot
* seaborn
* warnings
* font_manager (matplotlib) - for Korean font
* pandas
3. Algorithm
* Okt (konply.tag)
* re
* gensim
* word2vec (gensim.models)
* pandas
* pymongo
* math
* random

I. Crawling data from 'Melon' chart
--------------------------------
The main purpose of this project was to practice crawling skills.
- [Crawling song details in module](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/top_music/details.py)
- [Crawling user playlist in module](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/user/user_playlist.py)

II. Cleansing and exploring the gathered data
---------------------------------------------
The goal was to classify only into one genre and below is the code.
- [Renaming Genre](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/04_rename_genre.ipynb)
- [Visualizing data](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/05_visualize_data.ipynb)

III. Building algorithm for music recommendation
------------------------------------------------
I tried to think of creative ways to build a recommendation algorithm and came up with 2 kinds.
1. Insert year range and keyword. Used word2vec to find similarity between the keyword and some words from lyrics of the song which is used to recommend the song.
- [Analyzing song lyrics](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/recomm/lyrics_analysis.py)
2. Insert the sequence number of Melon playlist. The distribution of each genre in each year will be calculated and same goes to the user playlist. RMS will be calculated, smaller number between each year and the playlist means more similarity.
- [Measuring similarities between a year and the user playlist](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/recomm/ranking_random.py)

IV. Coding Flask and HTML to put algorithm in action
----------------------------------------------------
Run file to work in localhost
- [Flask + HTML](https://github.com/yeji0701/Crawling_Project/blob/master/recommendation/music.py)

Built with
----------
* 김예지
  * Crawling all data from Melon website and connecting DB to algorithm
  * Coding algorithm using lyrics of the song using word2vec, Natural Language Processing
  * Building Flask and HTML page for recommendation system
   * Github : https://github.com/yeji0701
* 김수경
  * Coding algorithm for measuring similarities between a year and the user playlist
  * Github : https://github.com/sukyeonging
 
Acknowledgements to our crawling site
-------------------------------------
- [Melon chart](https://www.melon.com/)
