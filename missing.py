# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'Age': [25, 30, np.nan, 45],
#     'Income': [50000, np.nan, 30000, np.nan],
#     'Name': ['Ali', 'Ahmed', None, 'Sara']
# })
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25,30, np.nan,45],
    'Income':[50000, np.nan, 30000, np.nan],
    'Name': ['Ali', 'Ahmed',None, 'Sara']
})

# method 01 using the .isnull().sum()
# by using this we will get the number of missing values in each columns 
print(df.isnull().sum())

# method 02 using the percentage .isnull().sum()/len(df)*100
print(df.isnull().sum()/len(df)*100)


# method 03 .info() used to find the null vlaues 
df.info()