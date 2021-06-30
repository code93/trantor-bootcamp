import os
from re import UNICODE
import sqlite3
from os import abort
from flask import Flask, redirect, render_template, request, url_for, flash, Response
from flask_login import LoginManager,UserMixin, login_required, login_user, logout_user, current_user
from models import BlogPost, UserModel,db,login
from flask_socketio import SocketIO
from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.debug = True

app.secret_key = 'xyz'
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db.init_app(app)
login.init_app(app)
login.login_view = 'login'

socketio = SocketIO(app)


@app.before_first_request
def create_all():
    db.create_all()
     
@app.route('/dashboard')
@login_required
def blog():
    return render_template('dashboard.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/dashboard')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/dashboard')
     
    return render_template('login.html')
 
@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/blogs')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')
 
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')



@app.route("/")
def Index():
    return render_template("Homepage.html")

@app.route("/Homepage")
def Homepage():
    return render_template("Homepage.html")


@app.route("/Contact")
def Contact():
    return render_template("Contact.html")


@app.route("/computer")
@login_required
def computer():
    return render_template("computer.html")

@app.route("/phone")
@login_required
def phone():
    return render_template("phone.html")

@app.route("/coffee")
@login_required
def coffee():
    return render_template("coffee.html")



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField("Post")


@app.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id
                             )
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('index'))

    return render_template('create_post.html', form=form)



@app.route('/index')
@login_required
def index():
    return render_template('index.html')