import numpy as np
a = np.array([1,3,7,2])
a[1:len(a)] = a[-1:0:-1]
print(a)