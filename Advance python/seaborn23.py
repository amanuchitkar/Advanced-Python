import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("tips")
# print(df) 
# df.boxplot(by='day',column=['total_bill'],grid=False)

titanic=sns.load_dataset("titanic")
print(titanic)
age1=titanic['age'].dropna()
# sns.distplot(age1,bins=30,kde=False)

data=sns.load_dataset("mpg")
# data.head()
# print(data)
sns.regplot(x="mpg",y="acceleration",data=data)
plt.show()