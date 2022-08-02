import numpy as np

a = np.arange(1,101).reshape(4, 25)

print(a.shape, a.dtype.name, a.size, a.itemsize)

b = np.array([1,2,3,4,6])
print(b)

c = np.array([1,2,3.6, 7.9, 15.2])
print(c, c.dtype.name)
