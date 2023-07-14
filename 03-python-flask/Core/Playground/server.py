from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return "hello"

@app.route('/play/')
def play():
    return render_template("index.html")

@app.route("/play/<int:x>")
def draw_boxes(x):
    return render_template("index2.html",x = x)

@app.route("/play/<int:x>/<color>")
def draw_boxes_color(x,color):
    return render_template("index2.html",x = x, color = color)

if __name__ == "__main__":
    app.run(debug=True) 