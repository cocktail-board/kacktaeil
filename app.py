from flask import Flask
from controller import test, register

app = Flask(__name__)
# 라우터가됨
app.register_blueprint(test.check, url_prefix='/')
app.register_blueprint(register.register, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')