import numpy as np
a=np.array([1,2,3,4,5])
print(a.shape)

b=np.array([[1,2,3,4],
            [5,6,7,8]])
rb=b.reshape(-1)
print(b.shape)

c=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# rc=c.reshape(6,2)
# rc=c.reshape(4,3)
# rc=c.reshape(2,2,3)
# rc=c.reshape(3,2,2)
rc=c.reshape(2,3,2)
print(rc)
print(rc.ndim)

