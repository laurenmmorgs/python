from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user


@app.route('/')
def index():
   return render_template('/index.html')


@app.route('/displaying_users')
def display_all_users():
   return render_template('showing_all.html', users = user.Users.get_all()) #all_posts must match the jinja in html 

@app.route('/create', methods=["POST"])
def adding_new_user():
   print(request.form)
   data = {
       "first_name":  request.form['first_name'],
       "last_name": request.form['last_name'],
       "email": request.form['email'],
   }
   this_user = user.Users.save(request.form)
   return redirect('/displaying_users')
