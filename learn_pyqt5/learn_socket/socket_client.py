# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/20 0020
import socket

class SocketClient:

    def __init__(self):
        self.sock = socket.socket()
        self.host = 'localhost'
        self.port = 10086

    def communicate(self):
        s = self.sock
        s.connect((self.host,self.port))
        for i in range(2):
            s.send(b'try to send you a message %d'%(i))
            result = s.recv(1024).decode('utf-8')
            if result:
                print(result)
        s.close()
if __name__ == "__main__":
    s = SocketClient()
    s.communicate()
