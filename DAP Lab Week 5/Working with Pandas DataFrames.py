import pandas as pd
data = np.array([['','Col1','Col2'], ['Row1',1,2], ['Row2',3,4]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))