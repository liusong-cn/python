import pandas as pd
import os

dfs = []
dir = '/Users/ls/Downloads/non_conver'
des = '/Users/ls/Downloads/non_conver.xlsx'
for root, dirs, files in os.walk(dir):
    for file in files:
        file_name = os.path.join(root, file)

        df = pd.read_excel(file_name)
        # print(df.loc[0,"sku_id"])
        for i in range(len(df)):
            d = str(df.loc[i,"task_id"])
            mid = len(d)//2
            df.loc[i,"task_id"] = '20' + d[0:mid] + '3' + d[mid:len(d)] + '1'

        dfs.append(df)
all_data = pd.concat(dfs)
all_data.rename(columns={'sku_id': 'sku_id',
                         'sku_name':'sku',
                         'parchage_num':'加购人数',
                         'order_num': '下单人数',
                         'payment_num': '付款人数',
                         'task_id': '任务id'
                        }, inplace=True)
# print(all_data.columns)

# all_data.to_excel(des, index=False, encoding='gbk')