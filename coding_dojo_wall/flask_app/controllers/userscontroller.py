from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from flask_app.models.post import Posts
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"


@app.route('/wall')
def users_wall():
   if 'user_id' not in session:
      return redirect('/')
   data = {
      'id': session['user_id']
   }
   return render_template('dashboard.html', current_user = user.Users.getByID(data),posts= Posts.get_users_with_posts(), dates = datetime )
