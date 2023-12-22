from common.httpclient import HttpClient

request = HttpClient()
url = "https://api.apiopen.top/api/login"
params = {"account": "309324904@qq.com",
          "password": "123456"}
res = request.send_request('post', url, params)
print(res.text)
print(res.headers)
print(res.cookies)
