from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '54e117fe7872d5a7e7e9ade1'
from scan import routes