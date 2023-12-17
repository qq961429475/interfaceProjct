from common.httpclient import HttpClient
import json


class TestLogin():
    request = HttpClient()

    def test_login(self):
        url = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
        data = {"username": "XXXXX", "password": "XXXXX"}
        res = self.request.send_request('get', url, data)
        print(res.text)
        assert res.status_code == 200
        assert json.loads(res.text)["msg"] == "登录成功"

    def test_login_fail(self):
        url = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
        data = {"username": "XXXXX", "password": "XXXXXX"}
        res = HttpClient().post(url, data)
        print(res.text)
        assert res.status_code == 200
        assert json.loads(res.text)["msg"] == "登录失败"
