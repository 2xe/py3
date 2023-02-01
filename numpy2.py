import numpy as np

data = np.loadtxt("experimental_results.txt")

a = data[:,0]
b = data[:,1]
c = np.average(a)
d = np.average(b)
print(c,d)

data_subset = b[0:500]
data_subset[:500] = 0

x = data[:,0]
y = data[:,1]
xx = np.average(x)
yy = np.average(y)
print(xx, yy)

