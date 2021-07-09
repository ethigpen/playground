from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", box=3, bcolor='lightblue')

@app.route('/play/<int:numx>')
def play_x(numx):
    return render_template('index.html', box=numx, bcolor='lightblue')

@app.route('/play/<int:num>/<string:color>')
def play_num(num,color):
    return render_template('index.html',box=num,bcolor=color)


if __name__=="__main__":
    app.run(debug=True)