import pandas as pd
s = pd.DataFrame(columns=['a','b'])
w = pd.DataFrame({'a':[5,3,4],'b':[9,3,6]})
print(w['b'].idxmin())
print(w)