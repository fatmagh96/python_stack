from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html" , x = 8, y=8, color1 = "black", color2 = "red")

@app.route('/<int:num>')
def y_axis(num):
    return render_template("index.html", x = int(num), y=8, color1 = "black", color2 = "red")


@app.route('/<int:num1>/<int:num2>')
def checkerboard(num1,num2):
    return render_template("index.html", x = num1 ,y = int(num2), color1 = "black", color2 = "red")


@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def checkerboard_colors(num1,num2, color1, color2):
    return render_template("index.html", x = num1 ,y = int(num2), color1 = color1, color2 = color2)


if __name__ == "__main__":
    app.run(debug=True)