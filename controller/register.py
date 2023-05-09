from flask import Blueprint, render_template

register = Blueprint('register', __name__)


@register.route('/')
def register_page():
    return render_template('/user/index.html')