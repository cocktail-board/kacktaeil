from flask import Blueprint, render_template

board = Blueprint('board', __name__)

@board.route('/board')
def board_list():
    return "게시판 보기"

@board.route('/board/save')
def board_create_get():
    return "게시판 생성 GET"

@board.route('/board/save', methods=["POST"])
def board_create_post():
    return "게시판 생성 POST"

@board.route('/board/delete', methods=["POST"])
def board_delete_get():
    return "게시판 삭제"

@board.route('/board/update', methods=["POST"])
def board_update_post():
    return "게시판 수정"
@board.route('/board/update')
def board_update_get():
    return "게시판 수정 화면"