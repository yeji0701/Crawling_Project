from flask import Flask, Markup, render_template, request
import song.recomm.ranking_random as rank
import song.recomm.lyrics_analysis as search

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('music/index.html')

@app.route('/music1', methods=['GET', 'POST'])
def music1():
    return render_template('music/music1.html')

@app.route('/music2', methods=['GET', 'POST'])
def music2():
    return render_template('music/music2.html')

@app.route('/music_result1', methods=['POST'])
def music_result1():
    year_end = int(request.form['year_end'])
    year_start = int(request.form['year_start'])
    look_keyword = request.form['look_keyword']
    result = search.search_similarity(year_end, year_start, look_keyword)
    result = result[['Artist', 'Title', 'Genre']].to_html(index=False, justify='center')

    result = Markup(result)

    return render_template('music/music_result1.html', table=result)

@app.route('/music_result2',  methods=['POST'])
def music_result2():
    seq = int(request.form['seq'])
    result = rank.top5_list(seq)
    result = result[['Artist', 'Title', 'Genre']].to_html(index=False, justify='center')

    result = Markup(result)

    return render_template('/music/music_result2.html', table=result)


if __name__ == "__main__":
    app.run(debug=True)