from flask import Flask , render_template, request, redirect, session

app  = Flask(__name__)
app.secret_key = "No Secrets in GitHub"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['username'] = request.form['username']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    session['flexRadioDefault'] = request.form['flexRadioDefault']
    return redirect('/result')

@app.route('/result')
def display():
    return render_template("display.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ =='__main__':
    app.run(debug = True, port=5003)