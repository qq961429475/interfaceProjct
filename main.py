import requests

url = 'http://127.0.0.1:5000/member/register'
params = {'username': 'gaofei', 'password': '12345'}
request = requests.post(url, params)
print(request.text)
