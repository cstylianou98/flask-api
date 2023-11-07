from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zickosbk:yiOXwiKC-acRdY0pVyi4zaJJS1ZHBdli@trumpet.db.elephantsql.com/zickosbk'
db = SQLAlchemy(app)

from application import routes