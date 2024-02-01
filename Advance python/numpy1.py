import numpy as np
# 0 D array
a=np.array(55)
print(a)
print(type(a))
print(a.ndim)

# 1 D array

b=np.array([1,2,3,4])
print(b)
print(type(b))
print(b.ndim)

# 2 D array

c=np.array([[1,2,3,4],
            [5,6,7,8]])
print(c)
print(type(c))
print(c.ndim)

# 2 D array

d=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(d)
print(type(d))
print(d.ndim)