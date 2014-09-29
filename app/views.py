import os
from flask import render_template, jsonify, request
from app import app
import pymysql as mdb

con = mdb.connect('localhost', "root", "ozfgefgvrwix", 'test1') 

@app.route('/')
@app.route('/index')
def index():
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Auctions LIMIT 12")
        rows = cur.fetchall()
        for key in rows:
            key['thumb'] = key['image'].split(".")[2] + "-thumb.jpg"
    return render_template('destination2.html', auctions=rows)

@app.route('/slides')
def cities_page():
    return render_template('slides_wide.html')

@app.route("/slides_wide", methods=["GET"])
def slides_wide():
    title="HammerPricer Slides"
    return render_template("slides_wide.html", title=title)
