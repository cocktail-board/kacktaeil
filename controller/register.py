from flask import Blueprint, render_template

register = Blueprint('register', __name__)


@register.route('/api/signup', methods=["POST"])
def register_page():
    return "회원가입"