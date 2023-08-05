from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'email_validation_db'

app  = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"