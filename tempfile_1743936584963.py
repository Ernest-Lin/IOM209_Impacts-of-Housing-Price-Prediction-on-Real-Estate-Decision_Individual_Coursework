# 导入必要的库
import pandas as pd  # 用于数据处理和分析的库
import numpy as np   # 用于数值计算的库

# 读取名为“房价预测.csv”的文件，并将其存储在变量ch中
ch = pd.read_csv('房价预测.csv')  
# 注意：这里出现了警告信息，提示某些列存在混合类型的数据。可以通过设置dtype参数或low_memory=False来解决。

# 检查“livingRoom”列中是否存在值为0的情况
0 in ch['livingRoom'].values  # 返回True，表示存在值为0的情况

# 查看“livingRoom”列中值为0的所有行
ch[ch['livingRoom'] == 0]  
# 输出结果显示有11行数据的“livingRoom”列值为0

# 统计“livingRoom”列中值为0的数量
(ch['livingRoom'] == 0).sum()  # 结果为11

# 删除“livingRoom”列中值为0的所有行
ch = ch[ch['livingRoom'] != 0]

# 再次统计“livingRoom”列中值为0的数量，确认是否删除成功
(ch['livingRoom'] == 0).sum()  # 结果为0，表示删除成功

# 查看数据框ch中各列的数据类型
ch.dtypes  
# 显示每一列的数据类型，发现部分列的数据类型不一致（如“livingRoom”为object而非数值型）

# 删除“url”列，因为该列对后续分析无用
ch = ch.drop(['url'], axis=1)

# 查看删除“url”列后的数据框ch
ch  

# 将处理后的数据保存到名为“删除url版.csv”的文件中
ch.to_csv("删除url版.csv", index=False)  
# 参数index=False表示保存时不去掉索引列

# 统计数据框ch中每一列的缺失值数量
ch.isnull().sum()  
# 发现“DOM”列缺失值过多（157972个），其他列也有少量缺失值

# 注释：由于“DOM”列缺失值过多，且"id"与"Cid"列对预测无帮助，决定删除这些列
# 发现DOM缺失值过多，因此应该删除，此外发现不仅是url无用，id与cid也对该数据预测无用，因此同时删除

# 删除“DOM”、“Cid”、“id”列
ch.drop(['DOM', 'Cid', 'id'], axis=1, inplace=True)  
# 参数inplace=True表示直接修改原数据框ch

# 获取初步处理后的数据
# 获取初步数据

# 将初步处理后的数据保存到名为“初步数据版.csv”的文件中
ch.to_csv("初步数据版.csv", index=False)
