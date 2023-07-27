from flask import Flask

app = Flask(__name__)
app.secret_key = "got a secret can you keep it"
DATABASE_NAME = "log-reg"