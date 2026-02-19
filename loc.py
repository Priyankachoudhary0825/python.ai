import pandas as pd
data=pd.Series([100, 200, 300, 400],
index=['x','y','z','w']) 
#1st Access the value
print(data.loc['y'])
# 2nd Access the elements
print(data.iloc[1])
# 3rd Access the multiple elements
print(data.loc[['x','w']]) 
# 4th Access last elements
print(data.iloc[-1])
#5th Access elements index 'y' to'z'
print(data.loc['y':'z'])
#6th difference between .iloc[2] and .ioc[]
print(data.iloc[2])
#
print(data.loc['2'])