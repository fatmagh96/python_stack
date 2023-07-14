from flask import Flask, render_template

app = Flask(__name__)


# http://127.0.0.1:5000/
# http://localhost:5000/
#(/)

@app.route('/') # Route (localhost:5000+/)
# Associated function
def index():
    return "Hello From Flask"

# http://127.0.0.1:5000/hi
@app.route('/hi')
def hi():
    return"<h1>Hi</h1>"

# http://127.0.0.1:5000/hi/USERNAME
@app.route('/hi/<username>')
def hi_user(username):
    return f"<h1>Hi {username}</h1>"

@app.route('/hi/<username>/<int:age>')
def user_info(username,age):
    return f"<h1>Username: {username} <br/> Age: {age}</h1>"


# http://127.0.0.1:5000/template
@app.route('/template')
def template():
    return render_template("index.html")

# http://127.0.0.1:5000/circles/color
@app.route('/circles/<url_color>/<int:number>')
def circles(url_color,number):
    print("*"*20, url_color,"*"*20)
    return render_template("index.html", color = url_color, number = number)





if __name__ == "__main__":
    app.run(debug=True)