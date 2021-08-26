# -*- coding:utf-8 -*-
# @auther: ls
# @date: 2021/8/26
import pandas as pd
import numpy as np


def pandas_demo():
    df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
                       'size': list('SSMMMLL'),
                       'weight': [8, 10, 11, 1, 20, 12, 12],
                       'adult': [False] * 5 + [True] * 2})
    print(df)

    # series允许不同类型的值
    s = pd.Series([1, 5, 2, 'a', np.nan])
    print(s)

    dates = pd.date_range('20130101', periods=6)
    df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df1)

    # 使用series字典生成DataFrame
    df2 = pd.DataFrame({
        'A':1.,
        # series对象作为一列
        'B':pd.Series(1,index=list(range(4)),dtype='float32'),
        'C': np.array([3]*4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"])
    })
    print(df2)

def pandas_data_view():
    """数据查看方式"""

    df2 = pd.DataFrame({
        'A': 1.,
        # series对象作为一列
        'B': pd.Series(1, index=list(range(4)), dtype='float32'),
        'C': np.array([3] * 4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"])
    })

    print(df2.head())

    print(df2.tail(2))

    print(df2.index)
    print(df2.columns)

    # 数据转置
    print(df2.T)


if __name__ == '__main__':
    # pandas_demo()
    pandas_data_view()