from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/countries")
def countries():

    conn = sqlite3.connect("dash_app/db/js_overload.sqlite")
    cur = conn.cursor()

    q = "SELECT Country, count(country) FROM jso11k GROUP BY Country"

    cur.execute(q)
    rows = cur.fetchall()

    data = []

    for row in rows:
        d = {}
        d[row[0]] = int(row[1])
        data.append(d)

    return jsonify(data)

if __name__ == "__main__":
    app.run()
