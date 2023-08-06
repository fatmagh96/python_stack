from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'login_and_registration_db'

app  = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"