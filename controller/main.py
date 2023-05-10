from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def main_get():
    message = '어서오세요 캌테일 로그인 화면입니다.'
    return render_template("user/index.html",message = message)