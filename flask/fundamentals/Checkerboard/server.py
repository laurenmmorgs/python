from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', rows=4, columns=4)

@app.route('/<int:y>')
def checks(y):
   return render_template('index.html', rows = 4, columns=y)

@app.route('/<int:x>/<int:y>')
def checking(x,y):
   return render_template('index.html', rows = x, columns = y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checking_colors(x,y,color1,color2):
   return render_template('index.html', rows = x, columns = y, color1 = color1, color2 = color2)

@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
   return 'Invalid URl'


if __name__=="__main__":
    app.run(debug=True)