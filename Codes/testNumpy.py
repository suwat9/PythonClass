import numpy as np

a = np.arange(1,101).reshape(4, 25)

print(a.shape, a.dtype.name, a.size, a.itemsize)

b = np.array([1,2,3,4,6])
print(b)

c = np.array([1,2,3.6, 7.9, 15.2])
print(c, c.dtype.name)

d = np.zeros((3,3),dtype=np.int16)
print(d)

e = np.ones((4,4),dtype=np.int16) 
print(e)

f = np.arange(10,31,5)
print(f)

g = np.linspace(1,100,50)
print(g)

seed = np.random.default_rng()

h = seed.random((1,10)) * 17
h = h.astype(np.int16)
print(h+1)
