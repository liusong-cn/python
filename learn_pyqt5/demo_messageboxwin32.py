# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/20 0020
# from tkinter import *
from tkinter import Tk
import tkinter.messagebox as m
import selenium
import win32api,win32con
import time

'''
经实验messagebox的父窗口tk也会弹出，继续研究，尝试使用selenium
后续发现可以父窗口withdraw
'''
def show_message():
    Tk().withdraw()
    m.showinfo('watch','this is a message')

#使用win32api可以无父窗口弹窗
def show_winmessage():
    win32api.MessageBox(0,'this is a message','title',win32con.MB_OK)
    #在没有主动关闭窗口时，线程阻塞，并没有执行等待3s，当主动关闭第一个窗口时才执行等待并打开下一个窗口
    time.sleep(3)
    win32api.MessageBox(0,'this is a message1','title',win32con.MB_OK)


def selenium_message():
    pass
# 直接输入main即可得到main入口
if __name__ == '__main__':
    show_message()
    # show_winmessage()

