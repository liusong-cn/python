# coding=utf-8
base_sql = "insert int table_a(id,name,value) values {values}"
datas = [[1,'lisi','abc']]*10
print(datas)


def single_sql():
    values = []
    for d in datas:
        id = d[0]
        name = d[1]
        value = d[2]
        values.append(f'({id},{name},{value})')
    value_str = ','.join(values)
    print(base_sql.format(values=value_str))

def multi_sql():
    values=[]
    for i in range(len(datas)):
        id, name, value = datas[i]
        values.append(f'({id},"{name}","{value}")')
        if (i+1)%3 == 0 or i == len(datas)-1:
            value_str = ','.join(values)
            print(base_sql.format(values=value_str))
            values = []

if __name__ == '__main__':
    # single_sql()
    multi_sql()