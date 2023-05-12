from flask import Blueprint, render_template, request, current_app, session,redirect, url_for
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

    # print(author)

    doc = {
        'title': title,
        'text': text,
        'images': img_url,
        'author': author, 
        'create_day': str(createday),
        'update_day': ''
    }

    db.board.insert_one(doc)

    return redirect(url_for('board.board_list'))


# 수정 버튼 누를시
@board.route('/board/update', methods=["POST"])
def board_update_post():
    board_title = request.form['board-title']
    board_date = request.form['board-date']

    result = list()
    kacktail_list = db.board.find_one({"title":board_title, "create_day":board_date})
    
    doc = {
        'id':str(kacktail_list['_id']),
        'title' : kacktail_list['title'],
        'text' : kacktail_list['text'],
        'images' : kacktail_list['images'],
        'author': kacktail_list['author']
    }
    result.append(doc)

    return render_template('user/main_page/board_update.html', kacktail_list = result)


# 수정 완료 누를시
@board.route('/board/update/finish', methods=["POST"])
def board_update_finish():
    id = request.form['board-id']
    title = request.form['title']
    text = request.form['text']
    img = request.files['img']
    img_url = '/img/'+img.filename
    update_date = dt.datetime.now().replace(microsecond=0)

    img.save(current_app.static_folder+'/img/'+img.filename)

    find_board = db.board.find_one({"_id":ObjectId(id)})

    author = str(find_board['author'])

    print(find_board)

    doc = {
        'title': title,
        'text': text,
        'images': img_url,
        'author': author, 
        'update_day': str(update_date),
    }
    

    db.board.update_one({"_id":ObjectId(id)},{"$set":doc})

    return redirect(url_for('my_page.my_page_route'))

# 삭제
@board.route('/board/delete', methods=["POST"])
def board_delete_get():
    board_date = request.form['board-date']

    db.board.delete_one({"create_day": board_date})

    return redirect(url_for('my_page.my_page_route'))