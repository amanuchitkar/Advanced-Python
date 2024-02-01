import matplotlib.pyplot as plt
import numpy as np
# points=np.array([[2,5,8,10,3,19,26,2,34],[0,5,8,10,3,19,26,2,34]])
points=np.array([2,5,8,10,3,19,26,2,34])
# plt.plot(points)

a2=np.array([1,9,3,8,5,4,7])
# plt.plot(a2,linestyle="dotted")

x=np.array(["x","y","z","w","e"])
y=np.array([20,10,29,90,19])
# plt.bar(x,y)

x1=np.array([32,45,10,56,28])
y1=np.array([3,0.2,.51,.48,.20])
# plt.scatter(x1,y1)


p=np.array([20,10,56,32,69])
# plt.pie(p)

h1=np.random.normal(170,209,301)
plt.hist(h1)
plt.show()