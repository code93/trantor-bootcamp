import os
from re import UNICODE
import sqlite3
from flask import Flask, redirect, render_template, request, url_for, flash, Response
from flask_login import LoginManager,UserMixin, login_required, login_user, logout_user, current_user
from forms import LoginForm




app = Flask(__name__)
app.debug = True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

conn=sqlite3.connect("froshims.db",check_same_thread=False)
cur= conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS login(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
email text not null,
password text not null);''')
conn.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = UNICODE(id)
         self.email = email
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id


@login_manager.user_loader
def load_user(user_id):
   conn = sqlite3.connect('froshims.db')
   curs = conn.cursor()
   curs.execute("SELECT * from login where id = (?)",[user_id])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])



@app.route("/hello")
def hello():
    if current_user.is_authenticated:
        return 'Hello %s!' % current_user.name
    else:
        return 'You are not logged in!'






@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Homepage")
def Homepage():
    return render_template("Homepage.html")



@app.route("/Login", methods=["get","post"])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    form = LoginForm()

    if form.validate_on_submit():
        conn = sqlite3.connect('froshims.db')
    
        curs = conn.cursor()
        curs.execute("SELECT * FROM login where email = (?)",    [form.email.data])
        user = list(curs.fetchone())
        Us = load_user(user[0])
        if form.email.data == Us.email and form.password.data == Us.password:
            login_user(Us, remember=form.remember.data)
            Umail = list({form.email.data})[0].split('@')[0]
            flash('Logged in successfully '+Umail)
            redirect(url_for('profile'))
        else:
            flash('Login Unsuccessfull.')
    return render_template('Login.html',title='Login', form=form)

       

@app.route("/Signup")
def Signup():
    return render_template("Signup.html")


@app.route("/Contact")
def Contact():
    return render_template("Contact.html")


@app.route("/register", methods=["GET","POST"])
def register():

    email = request.form.get("email")
    if not email:
        return render_template("error.html", message="Missing Email")
    
    password = request.form.get("password")
    if not password:
        return render_template("error.html", message="Missing Password")

    df = (email, password)
    
    cur.execute('''INSERT INTO login(email,password) VALUES(?,?)''', df)

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = cur.execute('''SELECT * FROM login''')
    return render_template("success.html", message="you are Logged IN!")


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,threaded=True)
