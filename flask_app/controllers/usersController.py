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
   data = {
       "first_name":  request.form['first_name'],
       "last_name": request.form['last_name'],
       "email": request.form['email']
   }
   user.Users.save(request.form)
   return redirect('/displaying_users')


@app.route('/user/delete/<int:user_id>')
def deletingUser(user_id):
   print(f'DELETING {user_id}')
   user.Users.deleteById({'id': user_id})
   return redirect('/displaying_users')

@app.route('/user/display/<int:user_id>')
def displaying_user(user_id):
   return render_template('displayingOneUser.html',
   dates = dateFormat, user = user.Users.getByID({'id': user_id}))


@app.route('/user/edit/<int:user_id>', methods = ['POST'])
def editingUsers(user_id):
   print(f'EDITING {user_id}')
   data = {
       "first_name":  request.form['first_name'],
       "last_name": request.form['last_name'],
       "email": request.form['email'],
       "id": user_id
   }
   updated = user.Users.editUser(data)
   # print(f' UPDATED {updated}')
   return redirect('/displaying_users')

@app.route('/user/<int:user_id>/edit')
def editing(user_id):
   return render_template('editingUser.html', user = user.Users.getByID({'id': user_id}))