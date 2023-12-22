#  配置全局token教程https://blog.csdn.net/m0_70102063/article/details/131556749
import jsonpath
import pytest
from common.httpclient import HttpClient
import requests


def pytest_collection_modifyitems(items):
    """
    当ids用例别名乱码时,confest里加
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    @pytest.mark.parametrize("input_title,",testdata["test_article"],ids=["新增文章"])
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='session', autouse=True)
def token():
    body = {'account': '309324904@qq.com', 'password': '123456'}
    url = 'https://api.apiopen.top/api/login'
    request = HttpClient()
    r = request.send_request('post', url, params=body)
    token = jsonpath.jsonpath(r.json(), '$..token')[0]
    return token
