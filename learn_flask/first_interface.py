# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/23 0023
from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():

    return 'hello_world'

if __name__ == '__main__':
    app.run()