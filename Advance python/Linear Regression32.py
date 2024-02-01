import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set = pd.read_csv('Salary_Data.csv')

print(data_set)
x = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 1].values
print(x)
print(y)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x_train, y_train)
y_pred = reg.predict(x_test)
x_pred = reg.predict(x_train)
# For Training set
# plt.scatter(x_train, y_train, color='green')
# plt.plot(x_train,x_pred,color='red')
# plt.show()

# For Test set
plt.scatter(x_test, y_test, color='blue')
plt.plot(y_test, y_pred, color='yellow')
plt.show()
