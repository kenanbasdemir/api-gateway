# import flask dependencies
from flask import Flask
# initialize the flask app
app = Flask(__name__)
# default route
@app.route('/')
def index():
    return 'Hello World!'
# create a route for webhook
#@app.route("/api/upload", methods=['POST'])
@app.route('/api/version')
def hello():
    return 'Version: 1.9.2'

# run the app
if __name__ == '__main__':
   #app.run()
   app.run(host='0.0.0.0', port=7003)
