#  配置全局token教程https://blog.csdn.net/m0_70102063/article/details/131556749
import jsonpath
import pytest
from common.httpclient import HttpClient


@pytest.fixture(scope='session', autouse=True)
def http_():
    request = HttpClient()
    return request


@pytest.fixture(scope='session', autouse=True)
def header1():
    body = {'account': '309324904@qq.com', 'password': '123456'}
    url = 'https://api.apiopen.top/api/login'
    request = HttpClient()
    r = request.send_request('post', url, params=body)
    token = jsonpath.jsonpath(r.json(), '$..token')[0]
    headers = {
        "token": token
    }
    return headers
