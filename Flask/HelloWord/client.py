# 模拟浏览器请求
import requests

'''
user_info = {
  'name': 'letian',
  'password': '123'
}
r = requests.post('http://127.0.0.1:5000/register', data=user_info)
'''

json_data = {'a': 1, 'b': 2}
r = requests.post('http://127.0.0.1:5000/add', json=json_data)

print(r.text)