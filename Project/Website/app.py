import sqlite3
from flask import Flask, redirect, render_template, request


app = Flask(__name__)

conn=sqlite3.connect("froshims.db",check_same_thread=False)
cur= conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS registrants(name TEXT, sport TEXT)''')
conn.commit()



SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/Homepage")
def Homepage():
    return render_template("Homepage.html")



@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Signup")
def Signup():
    return render_template("Signup.html")


@app.route("/Contact")
def Contact():
    return render_template("Contact.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    df = (name,sport)
    
    cur.execute('''INSERT INTO registrants(name,sport) VALUES(?,?)''', df)

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = cur.execute('''SELECT * FROM registrants''')
    return render_template("registrants.html", registrants=registrants)