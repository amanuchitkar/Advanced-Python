import pandas as pd


# def read_csv(file_name):
#     for chunk in pd.read_csv(file_name, chunksize=1):
#         yield chunk
#
#
# for df in read_csv("airport.csv"):
#     print(df)


df = pd.read_csv("airport.csv")
# print(df.head())

# print(df['type'].value_counts())
dfD = pd.get_dummies(df, columns=['type'])
# print(dfD)

df1=pd.read_csv("Iris.csv")
print(df1.head())
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
df1['Species']=le.fit_transform(df1['Species'])
print(df1)
