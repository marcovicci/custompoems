from flask import Flask, render_template, g, request
from random import shuffle
import sqlite3, random

app = Flask(__name__)
POEMDB = 'poem.db'

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/poem', methods=['POST'])
def poem():

    hairLike = request.form['hairs']
    eyesLike = request.form['eyes']
    genderLike = request.form['genders']

    db = sqlite3.connect(POEMDB)

    hairWords = []
    eyeWords = []
    genderWords = []

    print(genderLike)
    print(hairLike)
    print(eyesLike)

    cur = db.execute('SELECT detailed FROM colours WHERE basic LIKE' + '"' + hairLike + '"')
    for row in cur:
        hairWords.append(row[0])

    cur = db.execute('SELECT detailed FROM colours WHERE basic LIKE' + '"' + eyesLike + '"')
    for row in cur:
        eyeWords.append(row[0])

    cur = db.execute('SELECT * FROM genders WHERE gender LIKE' + '"' + genderLike + '"')
    for row in cur:
        genderWords.append(row[0])
        genderWords.append(row[1])
        genderWords.append(row[2])
        genderWords.append(row[3])
        genderWords.append(row[4])
        genderWords.append(row[5])
        genderWords.append(row[6])
        genderWords.append(row[7])
        genderWords.append(row[8])

    shuffle(eyeWords)
    shuffle(hairWords)

    db.close()
    return render_template(
        'yourpoem.html',
        HE = genderWords[2],
        HIS = genderWords[3],
        HIM = genderWords[4],
        HIMSELF = genderWords[5],
        BOY = genderWords[6],
        HEHAS = genderWords[7],
        HEIS = genderWords[8],
        EYES = eyeWords,
        HAIR = hairWords)
