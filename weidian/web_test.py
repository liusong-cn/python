from flask import Flask

import weidian

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return '<p>hello world</p>'

@app.route('/get_url')
def get_url():
    pay_url = weidian.flask()
    data = {'pay_url': pay_url}
    return data

if __name__ == '__main__':
    app.run(port=8080)