# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/20 0020
import socket

class SocketServer:

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 10086

    def publish(self):
        self.sock = socket.socket()
        s = self.sock
        s.bind((self.host,self.port))
        s.listen(5)

        while True:
            try:
                conn,addr = s.accept()
                conn.settimeout(5)
                #计数器不要放在第二个while内
                flag = 1
                while True:
                    result = conn.recv(1024).decode('utf-8')
                    #放在内部时，每一次进入第二个while都会重新赋值为1
                    # flag=1
                    if result:
                        print(result)
                        conn.send(b'this is my %dth response'%(flag))
                        flag+=1
                    # if flag > 10:break
                conn.close()
            except:
                print('has error')
                pass
if __name__ == "__main__":
    s = SocketServer()
    s.publish()