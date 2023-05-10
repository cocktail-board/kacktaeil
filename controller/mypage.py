from flask import Blueprint, render_template

my_page = Blueprint('my_page', __name__)

@my_page.route("/mypage")
def my_page_route():
    return "마이페이지 입니다."
