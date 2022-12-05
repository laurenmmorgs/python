from flask import render_template, request, redirect, session,flash
from flask_app import app
from flask_app.models import user
from datetime import datetime
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 
dateFormat = "%m/%d/%Y %I:%M %p"


@app.route('/')
def dashboard():

   return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
   if user.Users.validate_register(request.form):
      pw_hash =bcrypt.generate_password_hash(request.form['password'])
      data = {
         'first_name': request.form['first_name'],
         'last_name': request.form['last_name'],
         'email': request.form['email'],
         'password': pw_hash
      }
      session['user_id'] = user.Users.save(data)
      return redirect('/home')
   return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
   # data = { 'email' : request.form['email']} #? Do we need this? 
   user_in_db = user.Users.get_by_email(request.form)
   if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
         session['user_id'] = user_in_db.id
         print(user_in_db.id)
         return redirect('/home')
   #! If user is in data base then we pass user into session and then redirect to the dashboard, if user is not in database then we flash invalid 
   flash('Invalid Credentials!', 'loginError')
   return redirect('/home')


@app.route('/logout')
def logout():
   #clear session
   session.clear()
   return redirect('/')