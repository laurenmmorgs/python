from flask_app import app
from flask import render_template, session, redirect, request 
from flask_app.models import dojo
from flask_app.models import ninja


@app.route('/')
def index():
   return redirect('/dojos')

@app.route('/dojos')
def get_all():
   dojos = dojo.Dojos.get_all()
   return render_template('index.html', dojos=dojo.Dojos.get_all())

@app.route('/adding_dojo', methods=["POST"])
def adding_dojo():
   # data = {
   #    "name": request.form['name']  #? This doesn't have to be the same name as the value 
   # }
   #! SO we don't need to add this 
   dojo.Dojos.save(request.form)
   return redirect('/dojos')


@app.route('/displaying/ninjas/<int:dojo_id>')
def displaying_ninjas(dojo_id):
   data= {
      'dojo_id': dojo_id
   }
   return render_template('showing_ninjas.html', dojo = dojo.Dojos.get_ninja_with_dojos(data))
