from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def test():
    return "hello"

@app.route('/play')
def play():
    current_path = request.url_rule.rule
    print(current_path)
    return render_template("index.html", current_path = current_path)

@app.route("/play/<int:x>")
def draw_boxes(x):
    return render_template("index2.html",x = x)

@app.route("/play/<int:x>/<color>")
def draw_boxes_color(x,color):
    return render_template("index2.html",x = x, color = color)

if __name__ == "__main__":
    app.run(debug=True) 