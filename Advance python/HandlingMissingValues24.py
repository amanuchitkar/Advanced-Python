import pandas as pd

df = pd.read_csv('Placement_Data_Full_Class.csv')
# print(df)
dn = df.isnull().sum()
# print(dn)
df['salary']=df['salary'].fillna(df['salary'].mode()[0])
dn = df.isnull().sum()
# print(dn)
# print(df)

import numpy as np
from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
data=[[12,np.nan,34],[10,32,np.nan],[np.nan,11,20]]
print("original Data :\n",data)
imputer=imputer.fit(data)
data=imputer.transform(data)
print("Transform Data :\n",data)

