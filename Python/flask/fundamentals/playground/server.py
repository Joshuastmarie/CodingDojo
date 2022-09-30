from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Home Page"

@app.route('/play')
def three_boxes():
    return render_template("index.html", number = 3, color = "blue")

@app.route('/play/<int:number>')
def display_numbers(number):
    return render_template("index.html", number = number, color = "blue")

@app.route('/play/<int:number>/<string:color>')
def display_numbers_colors(number, color):
    return render_template("index.html", number = number, color = color)


if __name__=="__main__":
    app.run(debug=True)