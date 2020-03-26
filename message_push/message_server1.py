# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/25 0025
from flask_socketio import SocketIO,emit
from flask import Flask,render_template
from threading import Lock
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def foreground_show():
    '''
    模板目录需要在当前目录的templates/下，否则找不到file，或者在Flask初始化时配置模板路径
    :return:
    '''
    return render_template('index.html')

@socketio.on('connect','/test')
def handle_message():
    while True:
        data = random.randint(6)
        socketio.emit('server_response',{'data':data},namespace='/test')

if __name__ == '__main__':
    socketio.run(app,port=35000)