import numpy as np
a = np.array([5,3,8,1,6,9])
ind = np.where(a > 1,)
print(a[ind])