# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/25 0025
from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/publish")
def handle_message():
    message = request.args.get('message')
    if message:
        print(message)
        return 'success'
    else:
        return 'message is null'

def socket_push():
    pass

if __name__ == '__main__':
    app.run(port=9000)


