from flask import Blueprint, render_template, request, jsonify, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://gmakin36:vcAhbtS2O3CsZFxC@cocktail-cluster.zgihll4.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.kacktail


login = Blueprint('login', __name__)

@login.route('/api/login', methods=["POST"])
def postLogin():
    email_receive = request.form.get('login-email')
    pw_receive = request.form.get('login-password')

    find_user = db.users.find_one({"email":email_receive, "password":pw_receive})

    if find_user == None:
        return jsonify({"result":"failed"})
    
    session['id'] = str(find_user['_id'])
    # print(find_user)
    # print(session['id'])
    if find_user:
        return jsonify({"result":"success"})

@login.route("/api/logout", methods=["POST"])
def login_route():
    session.clear()
    message = '로그아웃 되었습니다.'
    return render_template('/user/index.html', message = message)
