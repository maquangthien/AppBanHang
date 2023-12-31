from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = '^%*&^^HJGHJGHJFD%^&%&*^*(^^^&^(*^^$%^GHJFGHJH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledbv1' % quote('PassW0rk#123Wen')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2

db = SQLAlchemy(app=app)
login = LoginManager(app=app)