from flask import Blueprint, render_template, jsonify, request, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
import certifi
import json

ca = certifi.where()
client = MongoClient('mongodb+srv://gmakin36:vcAhbtS2O3CsZFxC@cocktail-cluster.zgihll4.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.kacktail


my_page = Blueprint('my_page', __name__)

@my_page.route("/mypage")
def my_page_route():
    result = list()
    kacktail_list = list(db.board.find({},{'_id':False}))

    count = 1

    session_id = session['id']

    find_user = db.users.find_one({"_id":ObjectId(session_id)})

    name = find_user['name']

    for a in kacktail_list:
        if a['author'] == name:
            doc = {
                'title': a['title'],
                'text': a['text'],
                'images': a['images'],
                'author': a['author'],
                'create_day': a['create_day'],
                'count': count,
            }
            count = count+1
            result.append(doc)


    return render_template('/user/main_page/mypage.html', kacktail_list = result)

@my_page.route("/api/mypage", methods=["POST"])
def post_mypage():
    user_id = request.form.get('obj_id')    

    find_user = db.users.find_one({"_id":ObjectId(user_id)})

    return json.dumps(find_user, default=json_util.default)
