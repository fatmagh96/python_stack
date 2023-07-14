from flask import Flask

app = Flask(__name__)


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:name>")
def repeat(num, name):
    return f"{name}</br>"*num

@app.errorhandler(404)
def page_not_found(error):
    return "<h2>Sorry! No response. Try again.</h2>"

if (__name__) == '__main__':
    app.run(debug=True)