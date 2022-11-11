from flask import Flask  
app = Flask(__name__)


@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
   return 'Dojo!'

@app.route('/say/<string:things>')
def saying_things(things):
   print(things)
   return 'Hi ' + things

@app.route('/repeat/<int:number>/<string:stuff>')
def repeat_stuff(number,stuff):
   print(number)
   print(stuff)
   return(number * stuff)

@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return 'Sorry! No Reponse.Try again'

if __name__=="__main__":
    app.run(debug=True)