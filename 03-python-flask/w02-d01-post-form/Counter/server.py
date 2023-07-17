from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    # print(session)
    if 'count' in session:
        print('key exists!')
        session["count"] += 1
    else:
        print("key 'key_name' does NOT exist")
        session["count"] = 1
    return render_template("index.html")

@app.route('/plus_two')
def plus_two():
    session["count"] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)