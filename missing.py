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


# # method 01 using the .isnull().sum()
# # by using this we will get the number of missing values in each columns 
# print(df.isnull().sum())

# # method 02 using the percentage .isnull().sum()/len(df)*100
# print(df.isnull().sum()/len(df)*100)


# # method 03 .info() used to find the null vlaues 
# df.info()




# Checking types of missing values 



# =------------------Chekcing is MCAR  or not -============================

 #01 ==============little's mcar test ==================
# import pandas as pd
# import numpy as np
# from pyampute.exploration.mcar_statistical_tests import MCARTest

# np.random.seed(42)

# df = pd.DataFrame({
#     'Age': np.random.randint(20, 60, 100),
#     'Income': np.random.randint(30000, 100000, 100)
# })

# # Random missing values
# df.loc[np.random.choice(df.index, 15), 'Age'] = np.nan
# df.loc[np.random.choice(df.index, 10), 'Income'] = np.nan

# # mt = MCARTest(method="little")
# p_value = mt.little_mcar_test(df)

# print("P-value =", p_value)

# ===================finding correlation between missing values ------------============

print(df.isnull().astype(int))
print(df.isnull().astype(int).corr())