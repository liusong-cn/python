import pandas as pd
import os

dfs = []
dir = '/Users/ls/Downloads/bq_new2'
des = '/Users/ls/Downloads/bq_3d1.xlsx'
for root, dirs, files in os.walk(dir):
    for file in files:
        file_name = os.path.join(root, file)

        df = pd.read_excel(file_name)
        dfs.append(df)
all_data = pd.concat(dfs)
all_data.rename(columns={'dt': '日期',
                         'pin_count':'付款人数',

                         'pay_amount':'付款金额',
                         'non_bought_pin_count': '付款-未购人数',
                         'bought_pin_count': '付款-曾购人数',
                         'non_bought_pay_count': '付款-曾购金额',
                         'bought_pay_amount':'付款-未购金额'}, inplace=True)
# print(all_data.columns)

all_data.to_excel(des, index=False, encoding='gbk')