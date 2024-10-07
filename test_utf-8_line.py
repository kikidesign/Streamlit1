import pandas as pd
file_path = "penguins.csv"
data = pd.read_csv(file_path, encoding='GB2312')

f = open(file_path,"rb")# 二进制格式读文件
i = 0
while True:
    i += 1
    line = f.readline() # 按行读取

    if not line:
        break
    else:
        try:
            line.decode('ANSI')
        except: # 打印出不能通过'ANSI'方式解码的数据行
            print(i)
            print(str(line))
