from flask import Flask, render_template, g
import sqlite3, random

app = Flask(__name__)
EMOJIDB = 'emoji.db'

@app.route('/')
def index():

    randomEmojis = random.sample(range(15), 3)
    firstRng = randomEmojis[0]

    db = sqlite3.connect(EMOJIDB)

    emojiList = []
    cur = db.execute('SELECT * FROM emojis WHERE ID =' + str(randomEmojis[0]))
    for row in cur:
        emojiList.append(list(row))

    db.close()
    return render_template(
        'index.html',
        disclaimer='this will kill you',
        emojiOne=emojiList,
        rng = firstRng)

@app.route('/poem')
def poem():
    return render_template(
        'yourpoem.html')
