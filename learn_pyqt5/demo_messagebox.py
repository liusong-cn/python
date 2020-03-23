# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/20 0020
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QApplication,QWidget,QAction
import sys
'''
此种弹出消息框的方式需要父窗口的支持，比如有一个具有QMainWindow功能的，不能单独使用QMessageBox
后续发现应该有父窗口withdraw这类api来支持父窗口隐藏或退出
'''
class MyMessageBox(QMainWindow):

    def __init__(self):
        super(MyMessageBox, self).__init__()
        self.test_messagebox()

    def test_messagebox(self):
        menubar = self.menuBar()
        menu = menubar.addMenu('&File')
        click = QAction('tip',self)
        click.triggered.connect(self.message)
        menu.addAction(click)

        self.setGeometry(300, 300, 400, 150)
        self.show()
    def message(self):
        QMessageBox.information(self,'messagebox','this is a message',QMessageBox.Yes,QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MyMessageBox()
    sys.exit(app.exec_())