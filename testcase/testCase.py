import pytest

from common.httpclient import HttpClient
import jsonpath

request = HttpClient()

url1 = 'https://api.apiopen.top/api/login'
params = {'account': '309324904@qq.com', 'password': '123456'}
res1 = request.send_request('post', url1, params=params)
print(res1.json()['result']['token'])


class Test():
    request = HttpClient()
    baseurl = 'https://api.apiopen.top'

    token = None

    # def __init__(self):
    #     self.token = None

    def test_01(self):
        res = request.send_request('get', self.baseurl + '/api/sentences')

    def test_02(self):
        params = {'account': '309324904@qq.com', 'password': '123456'}
        request.send_request('post', self.baseurl + '/api/login', params=params)
        self.token = jsonpath.jsonpath(res1.json(), '$..token')[0]
        print(self.token)

    def test_03(self):
        # print(self.token)
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(["-s", "testCase.py"])
