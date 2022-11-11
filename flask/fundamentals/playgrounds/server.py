from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello World'

@app.route('/play')
def three_boxes():
   return render_template('index.html', times =3)

@app.route('/play/<int:num>')
def number_of_boxes(num):
   return render_template('index.html', times = num)

@app.route('/play/<int:num>/<color>')
def color_of_boxes(num,color):
   return render_template('index.html', 
   times = num, 
   color= color)

if __name__=="__main__":
    app.run(debug=True)