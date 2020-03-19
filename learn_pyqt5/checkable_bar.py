# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
import sys
from PyQt5.QtWidgets import QApplication,QAction,QMainWindow
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('default show')

        act = QAction('check',self,checkable=True)
        act.setCheckable(True)
        act.setStatusTip('view changed')
        #不是太明白triggered如何使toggle函数执行
        act.triggered.connect(self.toggle)

        menubar = self.menuBar()
        menu = menubar.addMenu('checkable')
        menu.addAction(act)

        self.setGeometry(300,300,400,150)
        self.setWindowTitle('this is a checkable menu')
        self.show()

    def toggle(self,state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())