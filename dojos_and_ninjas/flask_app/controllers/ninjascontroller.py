from flask_app.models import dojo
from flask_app.models import ninja
from flask_app import app
from flask import render_template, session, redirect, request


@app.route('/ninjas')
def new_ninja():
   return render_template('new_ninja.html', dojos= dojo.Dojos.get_all(), ninjas = ninja.Ninjas.get_all_ninjas())


@app.route('/create/ninja', methods =["POST"])
def adding_ninjas():
   dojo_id = request.form['dojo_id']
   data = {
      "first_name" : request.form['first_name'],
      "last_name" : request.form['last_name'],
      "age": request.form['age'],
      "dojo_id" : dojo_id
   }
   print(request.form)
   ninja.Ninjas.save(data)
   return redirect('/dojos')

