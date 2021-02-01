import numpy as np
import pandas as pd

##################作业1：求2+4+6+8+...+100的求和，用Python该如何写
sum=np.array(list(x*2 for x in range(1,51))).sum()
print(sum)

##################作业2：Action2: 统计全班的成绩
'''
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩
、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，
得出名次进行成绩输出（可以用numpy或pandas）
'''
data = {'姓名': ['张飞','关羽','刘备','典韦','许褚'], '语文': [68,95,98,90,80], '数学': [65,76,86,88,90], '英语': [30,98,88,77,90]}
df = pd.DataFrame(data, columns=list(data))
print(df.describe())

tags=df.columns[-3:]
df["总分"]=df[tags].sum(1)
df=df.sort_values("总分",ascending=False)
print(df)

##################作业3：对汽车质量数据进行统计
#Step1，数据加载
# 读取csv文档
data = pd.read_csv('.\car_data_analyze\car_complain.csv')

#Step2，数据预处理:拆分problem类型 => 多个字段
# 独热编码
cols=data["problem"].str.get_dummies(",")   #data["problem"]等同于data.problem
# 去掉problem列，添加problem列的独热编码
df=data.drop("problem",axis=1).join(cols)

#Step3，数据统计
#1) 品牌投诉总数
df['brand']=df['brand'].apply(lambda x: x.replace('一汽-大众','一汽大众'))
result=df.groupby(['brand'])['id'].agg(['count'])
result=result.sort_values("count",ascending=False)
print(result)
#2) 车型投诉总数
result=df.groupby(['car_model'])['id'].agg(['count'])
result=result.sort_values("count",ascending=False)
print(result)
#3) 哪个品牌的平均车型投诉最多
result=df.groupby(['brand','car_model'])['id'].agg(['count'])
result_pd=pd.DataFrame(list(result.index),columns=['品牌','车型']).join(pd.DataFrame(result.to_numpy(),columns=["投诉数"]))
result3=result_pd.groupby(['品牌']).agg({'车型':'count','投诉数':'sum'})
result3["平均车型投诉数"]=result3["投诉数"]/result3["车型"]
result3=result3.sort_values("平均车型投诉数",ascending=False)
print(result3)

