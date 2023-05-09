from flask import Flask
from controller import test, test2

app = Flask(__name__)
# 라우터가됨
app.register_blueprint(test.check, url_prefix='/')
app.register_blueprint(test2.signup, url_prefix='/signup')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')