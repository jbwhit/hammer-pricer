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

@app.route('/db')
def cities_page():
    with db: 
        cur = db.cursor()
        cur.execute("SELECT Name FROM City LIMIT 15;")
        query_results = cur.fetchall()
    cities = ""
    for result in query_results:
        cities += result[0]
        cities += "<br>"
    return cities

# @app.route('/realdestination', methods=['GET'])
@app.route('/realdestination')
def destination_2():
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Auctions")
        rows = cur.fetchall() 
    return render_template('destination2.html', auctions=rows)

@app.route("/auction")
def cities_page_fancy():
    # return render_template('main3.html') 
    return render_template('main4.html')

@app.route("/destination", methods=['GET'])
def train():
    keylookup = request.args.get("auctionurl")
    print keylookup.split("?")[0]
    # prediction = ""
    # for prices in ["$83,780", "$87,033", "$90,411"]:
    #     prediction += prices
    #     prediction += "<br>"
    prediction = {'low':"$23,780", 'value':"$27,033", 'high':"$30,411"}
    # prediction = ["$83,780", "$87,033", "$90,411"]
    return render_template('destination.html', prediction=prediction)

@app.route("/db_json")
def cities_json():
    with db:
        cur = db.cursor()
        cur.execute("SELECT Name, CountryCode, Population FROM city ORDER BY Population DESC;")
        query_results = cur.fetchall()
    cities = []
    for result in query_results:
        cities.append(dict(name=result[0], country=result[1], population=result[2]))
    return jsonify(dict(cities=cities))


# @app.route("/db_fancy")
# def cities_page_fancy():
#     with db:
#         cur = db.cursor()
#         cur.execute("SELECT Name, CountryCode, Population FROM City ORDER BY Population LIMIT 15;")

#         query_results = cur.fetchall()
#     cities = []
#     for result in query_results:
#         cities.append(dict(name=result[0], country=result[1], population=result[2]))
#     return render_template('cities.html', cities=cities) 
