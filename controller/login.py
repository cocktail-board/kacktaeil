from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route("/loginout", methods=["POST"])
def login_route():
    return "로그인아웃 화면"
