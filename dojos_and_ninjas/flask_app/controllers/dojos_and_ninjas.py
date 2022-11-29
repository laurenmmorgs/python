from flask_app.models import dojo
from flask_app.models import ninja
from flask_app import app
from flask import render_template, session, redirect, request 


@app.route('/')
def index():
   return redirect('/displaying_dojos')

@app.route('/displaying_dojos')
def get_all():
   dojos = dojo.Dojos.get_all()
   return render_template('index.html', dojos=dojo.Dojos.get_all())

@app.route('/adding_dojo', methods=["POST"])
def adding_dojo():
   data = {
      "name_of_dojo": request.form['name']  #? This doesn't have to be the same name as the value 
   }
   dojo.Dojos.save(request.form)
   return redirect('/displaying_dojos')

@app.route('/ninjas')
def new_ninja():
   return render_template('new_ninja.html', dojos= dojo.Dojos.get_all(), ninjas = ninja.Ninjas.get_all_ninjas())

@app.route('/create/ninja', methods =["POST"])
def adding_ninjas():
   data = {
      "first_name" : request.form['first_name'],
      "last_name" : request.form['last_name'],
      "age": request.form['age'],
      "dojo_id": request.form['dojo_id']
   }
   print(request.form)
   ninja.Ninjas.save(data)
   return redirect('/displaying_dojos')

@app.route('/displaying/ninjas/<int:dojo_id>')
def displaying_ninjas(dojo_id):
   print(dojo_id)
   dojo.Dojos.get_ninja_with_dojos({'dojo_id':dojo_id})
   return render_template('showing_ninjas.html')

# @app.route('/dojos/<int:dojo_id>')
# def dojos_and_ninjas(dojo_id):
#    print(f'This is the dojos id {dojo_id}')
#    return render_template('showing_ninjas.html', dojo = dojo.Dojos.get_ninja_with_dojos({'dojo_id':dojo_id}) )

# @app.route('/displaying/<int:dojo_id>')
# def displaying_dojo(dojo_id):
#    return render_template('showing_ninjas.html', dojo = dojo.Dojos.get_ninja_with_dojos(dojo_id))