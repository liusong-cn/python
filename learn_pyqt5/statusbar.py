# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/19 0019
from PyQt5.QtWidgets import (QWidget,QMainWindow,QApplication)
import sys

def two_helpful_fun():
    print(dir(QWidget))
    help(QWidget)

def write_help_doc():
    with open(r'd://qtwidge.txt','w') as f:
        sys.stdout = f
        help(QWidget)
#主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setui()
    def setui(self):
        self.statusBar().showMessage("toolbar")
        #设置几何尺寸，四个参数为从屏幕上x,y为起点设置宽高为w h
        self.setGeometry(300,300,400,150)
        self.setWindowTitle("status bar")
        self.show()

if __name__ == "__main__":
    # write_help_doc()
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())