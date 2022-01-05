import pydoc

import pandas as pd
import os
import random


def read_excel():
    df = pd.read_excel('/Users/ls/Downloads/babycare11-1.xlsx')
    data = df.head(2)
    print(str(data))
    # print(df.head(2))


def merge_excel():
    dfs = []
    dir = '/Users/ls/babycare/'
    des = '/Users/ls/babycare/babycare-stats-7-3.xlsx'
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_name = os.path.join(root, file)
            # print(root,"==",file)
            if 'babycare-stats-7-' in file_name:
                df = pd.read_excel(file_name)
                dfs.append(df)
        print(len(files))
    all_data = pd.concat(dfs)
    all_data.rename(columns={'dt': '日期', 'task_id': '任务ID', 'conversion_user_pin_count': '触达人数',
                             'conversion_bought_user_pin_count': '触达-曾购数',
                             'conversion_non_bought_user_pin_count': '触达-未购数',
                             'browsered_pin_count': '浏览数',
                             'browsered_bought_pin_count': '浏览-曾购数',
                             'browsered_non_bought_pin_count': '浏览-未购数',
                             'purchased_pin_count': '加购数',
                             'purchased_bought_pin_count': '加购-曾购数',
                             'purchased_non_bought_pin_count': '加购-未购数',
                             'ordered_pin_count': '下单数',
                             'ordered_bought_pin_count': '下单-曾购数',
                             'ordered_non_bought_pin_count': '下单-未购数',
                             'paid_pin_count': '付款数',
                             'paid_bought_pin_count': '付款-曾购数',
                             'paid_non_bought_pin_count': '付款-未购数',
                             'consume_amount': '付款额',
                             'consume_bought_amount': '付款-曾购金额',
                             'consume_non_bought_amount': '付款-未购金额',
                             'per_amount': '客单价',
                             'per_bought_amount': '客单价-曾购价',
                             'per_non_bought_amount': '客单价-未购价'}, inplace=True)
    # print(all_data.columns)

    all_data.to_excel(des, index=False, encoding='gbk')


def simulation():
    factor_low = 0.2
    factor_high = 0.6
    period_one_from = '/Users/ls/babycare/babycare-stats-1.xlsx'
    period_seven_from = '/Users/ls/babycare/babycare-stats-7.xlsx'
    period_one_des = '/Users/ls/babycare/babycare-stats-simu1.xlsx'
    period_seven_des = '/Users/ls/babycare/babycare-stats-simu7.xlsx'
    df = pd.read_excel(period_seven_from)
    # 某列
    # print(df.loc[:,'触达人数'])
    # 某单元格
    # print(df.loc[0,"触达人数"])
    # b = random.uniform(df.loc[0,'触达人数']*0.4,df.loc[0,'触达人数']*0.7)
    # b1 = round(b)
    # print(b)
    # print(b1)
    # print(df.head(1))
    # df.loc[0,'触达人数'] = 123
    # print(df.head(1))
    # print(len(df))

    for i in range(len(df)):
        pin_num = df.loc[i, '触达人数']
        pin_bought_num = round(random.uniform(pin_num * factor_low, pin_num * factor_high))
        pin_non_bought_num = pin_num - pin_bought_num
        df.loc[i, '触达-曾购数'] = pin_bought_num
        df.loc[i, '触达-未购数'] = pin_non_bought_num
        # 浏览
        brows_num = df.loc[i, '浏览数']
        brows_bought_num = round(random.uniform(brows_num * factor_low, brows_num * factor_high))
        brows_non_bought_num = brows_num - brows_bought_num
        df.loc[i, '浏览-曾购数'] = brows_bought_num
        df.loc[i, '浏览-未购数'] = brows_non_bought_num
        # 加购
        cart_num = df.loc[i, '加购数']
        cart_bought_num = round(random.uniform(cart_num * factor_low, cart_num * factor_high))
        cart_non_bought_num = cart_num - cart_bought_num
        df.loc[i, '加购-曾购数'] = cart_bought_num
        df.loc[i, '加购-未购数'] = cart_non_bought_num
        # 下单数
        order_num = df.loc[i, '下单数']
        order_bought_num = round(random.uniform(order_num * factor_low, order_num * factor_high))
        order_non_bought_num = order_num - order_bought_num
        df.loc[i, '下单-曾购数'] = order_bought_num
        df.loc[i, '下单-未购数'] = order_non_bought_num
        # 付款数
        paid_num = df.loc[i, '付款数']
        paid_bought_num = round(random.uniform(paid_num * factor_low, paid_num * factor_high))
        paid_non_bought_num = paid_num - paid_bought_num
        df.loc[i, '付款-曾购数'] = paid_bought_num
        df.loc[i, '付款-未购数'] = paid_non_bought_num
        # 付款额
        consume_amount = df.loc[i, '付款额']
        consume_bought_amount = round(random.uniform(consume_amount * factor_low, consume_amount * factor_high), 2)
        consume_non_bought_amount = consume_amount - consume_bought_amount
        df.loc[i, '付款-曾购金额'] = consume_bought_amount
        df.loc[i, '付款-未购金额'] = consume_non_bought_amount
        # 客单价
        df.loc[i, '客单价'] = 0 if df.loc[i, '付款额'] == 0 or df.loc[i, '下单数'] == 0 else round(
            df.loc[i, '付款额'] / df.loc[i, '下单数'], 2)
        df.loc[i, '客单价-曾购价'] = 0 if df.loc[i, '付款-曾购金额'] == 0 or df.loc[i, '下单-曾购数'] == 0 else round(
            df.loc[i, '付款-曾购金额'] / df.loc[i, '下单-曾购数'], 2)
        df.loc[i, '客单价-未购价'] = 0 if df.loc[i, '付款-未购金额'] == 0 or df.loc[i, '下单-未购数'] == 0 else round(
            df.loc[i, '付款-未购金额'] / df.loc[i, '下单-未购数'], 2)
    # print(df.loc[95,'付款额'])
    # print(df.loc[95,'付款额'] == 0)
    # print(round(df.loc[95,'付款-曾购金额']/df.loc[95,'下单-曾购数'],2))
    # print(type(df.loc[2,'付款-曾购金额']/df.loc[2,'下单-曾购数']))
    # print(type(df.loc[95,'付款额']))
    dfs = []
    dfs.append(df)
    data = pd.concat(dfs)
    data.to_excel(period_seven_des, index=False, encoding='gbk')


if __name__ == '__main__':
    # read_excel()
    merge_excel()
    # simulation()
