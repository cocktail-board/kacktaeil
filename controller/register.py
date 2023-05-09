from flask import Blueprint, render_template

register = Blueprint('register', __name__)


@register.route('/register')
def register_fun():
    return render_template('index.html')