# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
import sys
# print (sys.path)
from PyQt5.QtWidgets import QApplication,QMainWindow,qApp,QAction
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        #绝对和相对路径均可，但是路劲要双斜杠
        # exitAct = QAction(QIcon('D:\\pythonspace\\learn_pyqt5\\exit.jpg'),'$exit',self)
        exitAct = QAction(QIcon('exit.jpg'),'$exit',self)
        exitAct.setShortcut('CTRL+Q')
        exitAct.setStatusTip('exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        filemenu = menubar.addMenu('$file')
        filemenu.addAction(exitAct)

        self.setGeometry(300,300,400,150)
        self.setWindowTitle('simple menu')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
