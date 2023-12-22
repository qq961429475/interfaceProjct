import pytest
from common.httpclient import HttpClient
from confest import token


class Test:
    request = HttpClient()
    baseurl = 'https://api.apiopen.top'

    def test_01(self, token):
        r = self.request.send_request('get', self.baseurl + '/api/sentences')
        r.headers['token'] = token
        print(r.headers)
        assert 1 == 1

    def test_03(self, ):
        r = self.request.send_request('get', self.baseurl + '/api/sentences')
        print(r.json())
        print(r.headers)
        assert 1 == 1

    def test_04(self, token):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-s", "-v", "testCase.py"])
