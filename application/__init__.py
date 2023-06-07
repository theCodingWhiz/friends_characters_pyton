from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'e99c1fad75059f22db7778ba364edfa9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ozcktjxz:qPaBgc5CRkDwBNpMaeU9QVMcHV8Q34ql@lucky.db.elephantsql.com/ozcktjxz'

db = SQLAlchemy(app)  # Move the db initialization here

from application import forms, models, routes

if __name__ == '__main__':
    app.run()
