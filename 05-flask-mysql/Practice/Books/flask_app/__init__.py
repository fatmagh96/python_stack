from flask import Flask

# ! CHANGE DATABASE NAME
DATABASE = 'books_db'

app  = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhh"