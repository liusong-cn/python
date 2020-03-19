# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
from PyQt5.QtWidgets import QApplication,QMainWindow,qApp,QMenu
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('context menu')
        self.show()
    # 重写右键功能，当点击quit，退出系统
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newact = cmenu.addAction('new')
        quitact = cmenu.addAction('quit')
        opnact = cmenu.addAction('opn')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitact:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = Example()
    sys.exit(app.exec_())
