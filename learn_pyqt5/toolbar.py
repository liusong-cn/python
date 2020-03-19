# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setui()
    def setui(self):

        action = QAction(QIcon('exit.jpg'),'usetoolbar',self)
        action.triggered.connect(qApp.quit)
        #标准命令不区分大小写
        action.setShortcut('ctrl+q')
        #toolbar的名称没展示出来
        self.toolbar = self.addToolBar('my toolbar')
        self.toolbar.addAction(action)

        self.setGeometry(300,300,400,150)
        self.setWindowTitle('toolbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

