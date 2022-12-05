from flask import render_template, request, redirect, session,flash
from flask_app import app
from flask_app.models import user
from flask_app.models.post import Posts
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"



@app.route('/post', methods=['POST'])
def post():
   data = {
      'content' : request.form['content'],
      'user_id': session['user_id']
   }
   Posts.save(data)
   Posts.get_users_with_posts()
   return redirect('/wall')
