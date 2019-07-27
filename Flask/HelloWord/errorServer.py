from flask import Flask, abort, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/user')
def user():
  abort(401)

@app.errorhandler(401)
def page_unauthorized(error):
  return render_template_string('<p>{{ error_info }}</p>', error_info=error), 401

if __name__ == '__main__':
  app.run(debug=True)