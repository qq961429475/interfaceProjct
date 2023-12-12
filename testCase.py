import unittest
from common.httpclient import HttpClient


class TestAPIDemo(unittest.TestCase):
    token = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.request = HttpClient()

    def test02(self):
        res = self.request('get', 'https://api.apiopen.top/api/getTime')
        print(res.json())
        assert res.json()['code'] == 200

    def test03(self):
        res = self.request('get', 'https://api.apiopen.top/api/sentences')
        print(res.json())


if __name__ == '__main__':
    unittest.main()
