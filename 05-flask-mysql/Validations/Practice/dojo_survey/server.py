from flask import Flask , render_template, request, redirect, session
from ninja import Ninja

app  = Flask(__name__)
app.secret_key = "No Secrets in GitHub"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("REQUEST FORM/ ",request.form, "////////////////////////////////////")
    if Ninja.validate(request.form):
        ninja_id = Ninja.create_ninja(request.form)
        session['id'] = ninja_id
        print("----------------",ninja_id,"-----------------")
        return redirect('/result')
    print("NOT VALID")
    return redirect('/')

@app.route('/result')
def display():
    print("SESSION ******", session['id'])
    ninja = Ninja.get_info(session['id'])
    return render_template("display.html",ninja = ninja)

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ =='__main__':
    app.run(debug = True, port=5003)