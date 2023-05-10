from flask import Blueprint, render_template

board = Blueprint('board', __name__)

@board.route("/board")
def board_select():
    return "게시글 조회"


@board.route("/board/save")
def board_select():
    return "게시글 조회"