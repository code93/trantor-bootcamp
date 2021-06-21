import sqlite3
from flask import Flask, redirect, render_template, request


app = Flask(__name__)

conn=sqlite3.connect("froshims.db",check_same_thread=False)
cur= conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS registrants(email TEXT, password TEXT)''')
conn.commit()




@app.route("/")
def index():
    return render_template("index.html")

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

    email = request.form.get("email")
    if not email:
        return render_template("error.html", message="Missing Email")
    
    password = request.form.get("password")
    if not password:
        return render_template("error.html", message="Missing Password")

    df = (email, password)
    
    cur.execute('''INSERT INTO registrants(email,password) VALUES(?,?)''', df)

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = cur.execute('''SELECT * FROM registrants''')
    return render_template("success.html", message="you are Logged IN!")