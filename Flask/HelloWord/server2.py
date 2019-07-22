from flask import Flask, request, Response, jsonify
import json

app = Flask('client2')

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/add', methods=['POST'])
def add():
  result = {'sum': request.json['a'] + request.json['b']}
  '''
  return Response(json.dumps(result), mimetype='application/json')
  '''
  '''
  resp = Response(json.dumps(result), mimetype='application/json')
  resp.headers.add('Server', 'python flask')
  return resp
  '''
  return jsonify(result)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)