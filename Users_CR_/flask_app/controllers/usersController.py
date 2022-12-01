from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
app.secret_key = 'unique key'


@app.route('/')
def index():
   return render_template('/index.html')


@app.route('/displaying_users')
def display_all_users():
   return render_template('showing_all.html', users = user.Users.get_all()) #all_posts must match the jinja in html 

@app.route('/create', methods=["POST"])
def adding_new_user():
   session['first_name'] = request.form['first_name']
   session['last_name'] = request.form['last_name']
   session['email'] = request.form['email']
   if not user.Users.validate_user(session):
      return redirect('/')
   data = {
       "first_name":  request.form['first_name'],
       "last_name": request.form['last_name'],
       "email": request.form['email'],
   }
   user.Users.save(request.form)
   return redirect('/displaying_users')


@app.route('/register', methods=['POST'])
def registration():
   if not user.Users.validate_user(request.form):
      return redirect('/')
   user.Users.save(request.form)
   return redirect('/')