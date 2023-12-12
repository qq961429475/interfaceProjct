from flask import Flask, request

app = Flask("py44")


@app.route('/member/register', methods=['post'])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == 'gaofei' and password == '123456':
        return {"code": 10, "msg": "success"}
    elif username == 'gaofei':
        return {"code": 20, "msg": "password error"}
    else:
        return ''


app.run(debug=True)
