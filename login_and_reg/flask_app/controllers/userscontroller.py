from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"


@app.route('/home')
def index():
   if 'user_id' not in session:
      return redirect('/')
   data = {
      'id': session['user_id']
   }
   return render_template('dashboard.html', current_user = user.Users.getByID(data) )
