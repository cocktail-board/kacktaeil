from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def main_get():
    return render_template("user/index.html")