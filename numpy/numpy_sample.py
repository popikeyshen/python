
import numpy as np
import sys


a = np.array([1,2,3,4,5,6], float)
print(a, type(a), a[:2], sys.getsizeof(a), "96+8*n for float", a.shape, a.dtype)

print(2 in a, a.reshape(3,2), a.flatten(), np.concatenate((a,np.array([7,8,9],float)))  )

a.sort()
b = np.array([1,5,3,1,2,6], float)
print( a.mean(axis=0), a, a.clip(2, 5), np.unique(a), a>b, np.where(b > 3) , np.dot(a, b)) #a.diagonal()
