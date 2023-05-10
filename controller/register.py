from flask import Flask,Blueprint, render_template, request
import datetime as dt   
from pymongo import MongoClient   
register = Blueprint('register', __name__)

app = Flask(__name__)
#client = MongoClient('mongodb+srv://:@cluster0.xqvi6vf.mongodb.net/?retryWrites=true&w=majority')
#db = client.dbsparta

@register.route('/api/signup', methods=["POST"])
def register_page():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    createday = dt.datetime.now().replace(microsecond=0)

    message = '회원가입에 성공하셨습니다.'
    #DN 저장한다.

    return render_template("user/index.html", message=message)

