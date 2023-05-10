from flask import Blueprint, render_template, request, current_app, session
from werkzeug.utils import secure_filename
from pymongo import MongoClient  
from bson.objectid import ObjectId
import certifi
import datetime as dt   

ca = certifi.where()

board = Blueprint('board', __name__)

client = MongoClient('mongodb+srv://gmakin36:vcAhbtS2O3CsZFxC@cocktail-cluster.zgihll4.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.kacktail

@board.route('/board')
def board_list():
    result = list()
    kacktail_list = list(db.board.find({},{'_id':False}))

    count = 1

    for a in kacktail_list:
        doc = {
            'title': a['title'],
            'text': a['text'],
            'images': a['images'],
            'author': a['author'],
            'count': count,
        }
        count = count+1
        result.append(doc)
    return render_template('user/main_page/index.html',kacktail_list = result)

@board.route('/board/save')
def board_create_get():
    return render_template('user/main_page/board_create.html')

@board.route('/board/save', methods=["POST"])
def board_create_post():
    title = request.form['title']
    text = request.form['text']
    img = request.files['img']
    img_url = '/img/'+img.filename
    createday = dt.datetime.now().replace(microsecond=0)

    img.save(current_app.static_folder+'/img/'+img.filename)

    session_id = session['id']

    find_user = db.users.find_one({"_id":ObjectId(session_id)})

    author = str(find_user['name'])

    print(author)

    doc = {
        'title': title,
        'text': text,
        'images': img_url,
        'author': author, 
        'create_day': createday,
        'update_day': ''
    }

    db.board.insert_one(doc)

    result = list()
    kacktail_list = list(db.board.find({},{'_id':False}))

    count = 1

    for a in kacktail_list:
        doc = {
            'title': a['title'],
            'text': a['text'],
            'images': a['images'],
            'author': a['author'],
            'count': count,
        }
        count = count+1
        result.append(doc)
    return render_template('user/main_page/index.html',kacktail_list = result)

@board.route('/board/delete', methods=["POST"])
def board_delete_get():
    return "게시판 삭제"

@board.route('/board/update', methods=["POST"])
def board_update_post():
    return "게시판 수정"
@board.route('/board/update')
def board_update_get():
    return "게시판 수정 화면"