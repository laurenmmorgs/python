from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase='hello',times=4)

    
@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return 'Invalid URL'

if __name__=="__main__":
    app.run(debug=True)