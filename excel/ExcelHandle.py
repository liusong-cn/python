# -*- coding:utf-8 -*-
# @auther: ls
# @date: 2021/8/18

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_excel():
    con = pd.read_excel('智能营销 - 任务进度.xlsx')
    df = pd.DataFrame(con)
    print('excel维度: {}'.format(df.shape))
    print('excel基本信息: {}'.format(df.info))
    print('excel每一列格式: {}'.format(df.dtypes))
    # 执行head命令
    print(con.head())


def read_excel_and_convert():
    df = pd.DataFrame(pd.read_excel(r'智能营销 - 任务进度.xlsx', converters={'任务描述': convert_cell}))
    print(df)


def convert_cell(cell):
    if (cell == '【营销版-运营端】代运营投放计划'):
        return cell + 'abc'
    return cell


def write_excel():
    identi_info = pd.DataFrame({
        'name': ['zhangsan', 'lisi', 'wangwu'],
        'age': [1, 2, 3],
        "height": [1.67, 1.70, 1.83]
    })

    city_info = pd.DataFrame({
        'city_name': ['chengdu', 'guiyang', 'hangzhou'],
        'population': [1600, 800, 700]
    })

    with pd.ExcelWriter('target.xls') as writer:
        identi_info.to_excel(writer, sheet_name='identi')
        city_info.to_excel(writer, sheet_name='city')


def draw_picture1():
    """
    多个坐标轴
    """
    fig, axes = plt.subplots(nrows=2, ncols=2)
    axes[0, 0].set(title='upper left')
    axes[0, 1].set(title='upper right')
    axes[1, 0].set(title='lower left')
    axes[1, 1].set(title='lower right')
    plt.show()


def draw_picture0():
    """单个坐标轴"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='an example', ylabel='y-axis', xlabel='x-axis')
    plt.show()

def draw_picture2():
    """使用numpy绘制三角函数曲线"""
    x = np.linspace(0, np.pi)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    # 绘图
    axes.plot(x, sin_x)
    plt.show()


if __name__ == "__main__":
    # read_excel()
    # read_excel_and_convert()
    # write_excel()
    # draw_picture1()
    # draw_picture0()
    draw_picture2()