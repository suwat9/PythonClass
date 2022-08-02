import numpy as np

a = np.arange(1,101).reshape(4, 25)

print(a.shape, a.dtype.name, a.size, a.itemsize)
