from flask import Blueprint, render_template

check = Blueprint('test', __name__)

# 이후 경로 입력, 함수명과 라우트 이름이 같으면안됨
# http://localhost:5001/
@check.route('/')
def checked():
    return render_template('index.html')