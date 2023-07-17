from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    dt_string = datetime.now().strftime("%B %d %Y %I:%M:%S %p")
    sum = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} for {sum} fruits")
    return render_template("checkout.html", num_strawberries = request.form['strawberry'], num_rasberries = request.form['raspberry'],num_apples = request.form['apple'],first_name = request.form['first_name'],last_name = request.form['last_name'], student_id = request.form['student_id'], sum = sum , datetime = dt_string)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    