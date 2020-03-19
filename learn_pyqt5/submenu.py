# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
from PyQt5.QtWidgets import QApplication,QMenu,QMainWindow,QAction
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setui()

    def setui(self):

        menu = self.menuBar()
        filemenu = menu.addMenu("file")

        impmenu = QMenu("subment",self)
        impact = QAction('import mail',self)
        impmenu.addAction(impact)

        newact = QAction('new',self)
        filemenu.addAction(newact)
        filemenu.addMenu(impmenu)

        self.setGeometry(300,300,400,300)
        self.setWindowTitle("submenu")
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

