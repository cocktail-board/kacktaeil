from flask import Blueprint, render_template, session

main = Blueprint('main', __name__)

@main.route("/")
def main_get():
    message = '어서오세요 캌테일 로그인 화면입니다.'
    return render_template("user/index.html",message = message)

@main.route("/index")
def mainIndex():
    return render_template("user/main_page/index.html")