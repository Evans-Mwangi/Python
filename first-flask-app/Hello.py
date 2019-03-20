import sqlite3
from flask import Flask,render_template, request

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.route('/')
def hello():
    return 'Hello World!'

app.debug =  True
app.run()