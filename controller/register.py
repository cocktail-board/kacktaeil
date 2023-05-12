from flask import Flask,Blueprint, render_template, request
import datetime as dt   
from pymongo import MongoClient   
import certifi
register = Blueprint('register', __name__)

ca = certifi.where()

app = Flask(__name__)
client = MongoClient('mongodb+srv://gmakin36:vcAhbtS2O3CsZFxC@cocktail-cluster.zgihll4.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.kacktail

@register.route('/api/signup', methods=["POST"])
def register_page():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    createday = dt.datetime.now().replace(microsecond=0)

    user_list = list(db.users.find({},{'_id':False,'name':False,'password':False,'createday':False}))

    check = True

    for user in user_list:
        if(email == user['email']):
            check = False

    if(check):
        message = '회원가입에 성공하셨습니다.'
        doc = {
            'name': name,
            'nickname': '',
            'email': email,
            'password': password,
            'createday': createday
        }
        print(doc)
        db.users.insert_one(doc)
    else:
        message = '이메일이 존재합니다.'

    return render_template("user/index.html", message=message)

