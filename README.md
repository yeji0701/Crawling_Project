Crawling + Flask Project
========================
This project started off from a question: "Past fashion trend came back as 'newtro (new + retro)', so can music trend come back too?" 
The primary purpose was to crawl music data in the years 1960s~20100s from a music chart to explore and visualize. During this process, came an idea for a music recommendation system to answer another question: "What kind of modern music will a person with a playlist from the past listen to?"

The major activities in this project:
* Crawling data from 'Melon' chart
* Cleansing and exploring the gathered data
* Building algorithm for music recommendation
* Coding Flask and HTML to put algorithm in action

Built with:
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

I. Crawling data from 'Melon' chart
--------------------------------
The main purpose of this project was to practice crawling skills.
Below are the links to the code used for crawling the melon chart for song Title, Artist, Year, Genre, Lyrics.
- [Crawling Melon chart (시대별 차트)](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/01_crawling_melon_chart(1).ipynb)
- [Crawling Genre of each song](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/02_crawling_melon_chart(2).ipynb)
- [Crawling Lyrics of each song](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/06_crawling_melon_chart(3).ipynb) 

Same process was used for crawling the Melon user playlist.

These are compiled in a module:
- [Crawling song details in module](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/top_music/details.py)
- [Crawling user playlist in module](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/song/user/user_playlist.py)

II. Cleansing and exploring the gathered data
---------------------------------------------
First thing to do was regrouping the genre because many of the songs were categorized in a mix of different genres. The goal was to classify only into one genre and below is the code for to doing so.
- [Renaming Genre](https://github.com/yeji0701/Crawling_Project/blob/master/crawling_code/04_rename_genre.ipynb)

1. Number of songs per genre, year grouped to 5 years (except 1964-1969)
- From this, we can see the songs were mostly '성인가요' in the 1960s to early 1970s. As time passes, the type of music diversified to what we can see in the last chart.
![image](https://user-images.githubusercontent.com/28764376/101884123-92b2cc80-3bdb-11eb-9b5b-84aa87b1c9a0.png)

2. Increase and decrease of the number of genre over time
- From this, we can see the movement of the number of songs per genre over the years
![image](https://user-images.githubusercontent.com/28764376/101886836-6600b400-3bdf-11eb-8833-9a9ad0528458.png)

III. Building algorithm for music recommendation
------------------------------------------------
I tried to think of creative ways to build a recommendation algorithm and came up with 2 kinds.
1. Analyzing song lyrics
2. Measuring similarities between a year and the user playlist
