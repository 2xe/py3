import numpy as np
import math as m

throws = []

def throwTwoDiceAndReturnSum(diceSizeOne, diceSizeTwo, throws):
	c = (np.random.randint(1,diceSizeOne+1,throws) + np.random.randint(1,diceSizeTwo+1,throws))
	return c

#throws.append(throwTwoDiceAndReturnSum(12,6,10000))

#print(np.average(throws))

#print(np.array([[1,2,3,4], [5,6,7,8], [0,0,0,0]]))

a = np.array([[1,2,3,4], [5,6,7,8], [0,0,0,0]])
b = np.array([[1,2,3,4], [5,6,7,9], [0,0,0,0]])

mask = a != b

print(b[mask], a[mask])