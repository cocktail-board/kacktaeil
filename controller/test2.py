from flask import Blueprint

signup = Blueprint('test2', __name__)

# 이후 경로 입력
# http://localhost:5001/signup
@signup.route('/')
def signupaa():
    return '블루프린트 테스트 중입니다. 회원가입'