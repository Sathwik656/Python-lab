import pandas as pd
import numpy as np

data = np.arange(6)
df = pd.DataFrame(data,index=['a','b','c','d','e','f'],columns=['one'])
print("Original data frame: \n",df)
print("Head (2 rows:) \n",df.head(2))
print("Tail (2 rows:) \n",df.tail(2))

column1 = df['one']
print("Column 'one' : \n",column1)

new_column = pd.Series([3,4,5,6,7,8],index=['a','b','c','d','e','f'],name='four')
df=pd.concat([df,new_column],axis=1)
print("After appending: \n",df)

agg = df.aggregate({'sum','max','mean'})
print("Aggrigate functions: \n",agg)