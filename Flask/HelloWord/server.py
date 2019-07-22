from flask import Flask, request

'''
__name__ 的值为字符串 __main__
'''
app = Flask(__name__)

# app = Flask('my-app', static_folder='path1', template_folder='path2')

@app.route('/')
def hello_world():
  return 'Hello World'
  # print(request.path)
  # print(request.full_path)
  # return request.args.__str__()
  # return request.args.get('info')
  '''
  r = request.args.get('info')
  if r == None:
    return ''
  return r
  
  r = request.args.getlist('p')
  return str(r)
  '''

# methods=['GET', 'POST']
'''
@app.route('/register', methods=['POST'])
def register():
  print(request.headers)
  # print(request.stream.read())
  print(request.form)
  print(request.form['name'])
  print(request.form.get('name'))
  print(request.form.getlist('name'))
  print(request.form.get('nickname', default='little apple'))
  return 'welcome'
'''

@app.route('/add', methods=['POST'])
def add():
  print(request.headers)
  print(type(request.json))
  print(request.json)
  result = request.json['a'] + request.json['b']
  return str(result)

if __name__ == '__main__':
  # debug=True
  app.run(port=5000)
