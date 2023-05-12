from flask import Flask
from controller import admin_page, register,mypage,board,login,main

application = app = Flask(__name__)

# 라우터가됨
app.register_blueprint(admin_page.admin, url_prefix='/')
app.register_blueprint(register.register, url_prefix='/')
app.register_blueprint(main.main, url_prefix="/")
app.register_blueprint(mypage.my_page, url_prefix="/")
app.register_blueprint(board.board, url_prefix="/")
app.register_blueprint(login.login, url_prefix="/")

if __name__ == '__main__':
    app.secret_key = "ewf*(#JFnowef*@(0F|QW{F|}))"
    
    app.run()