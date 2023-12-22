import json

from flask import Flask, request

app = Flask("py44")


@app.route('/member/register', methods=['post'])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    if username == 'gaofei' and password == '123456':
        return {"code": 10, "msg": "success"}
    elif username == 'gaofei' and password == '12345':
        return {"code": 20, "msg": "password error"}
    else:
        return ''


# 定义视图函数，设置路由规则
@app.route("/index")  # method没有默认get
def index():
    print("欢迎访问index主页")
    return "hello mock"


# {"username":"test_login","password":"123456"}
@app.route("/login", methods=["POST"])
def login():
    # request.get_data()用于获取请求中的原始数据，返回一个字节字符串，包含请求的主体内容
    result = json.loads(request.get_data().decode("utf-8"))
    username = result.get("username")
    password = result.get("password")
    print(username, password)
    if username == "gaofei" and password == "123456":
        data = {
            "success": True,
            "code": 666,
            "message": "恭喜登录成功",
            "token": "qiow-8124-uiqw-1232"
        }
    else:
        data = {
            "success": False,
            "code": 0000,
            "message": "账号或密码错误，请稍后重试！",
            "token": None
        }
    return data


if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1", debug=True)
