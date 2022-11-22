from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/')
def index():
   return render_template('/index.html')


@app.route('/displaying_users')
def display_all_users():
   return render_template('showing_all.html', users = user.Users.get_all(), dates = dateFormat) #all_posts must match the jinja in html 

@app.route('/create', methods=["POST"])
def adding_new_user():
   print(request.form)
   data = {
       "first_name":  request.form['first_name'],
       "last_name": request.form['last_name'],
       "email": request.form['email']
   }
   this_user = user.Users.save(request.form)
   # delete_user = user.Users.deleteById(request.form)
   return redirect('/displaying_users')


@app.route('/user/delete/<int:user_id>')
def deletingUser(user_id):
   # print(f'User clicked being deleted:{user_id}')
   user.Users.deleteById({'id': user_id})
   return redirect('/user/display/<int:user_id>')

@app.route('/user/display/<int:user_id>')
def displaying_user(user_id):
   # print(f'User clicked being deleted:{user_id}')
   user.Users.deleteById({'id': user_id})
   return index.html('displayingOn')

