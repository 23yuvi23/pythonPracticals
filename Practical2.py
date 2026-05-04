import pandas as pd
import numpy as np

data = {
    'Name':['Rahul','Ram','Aman',np.nan],
    'Age' :[21, np.nan,23,44],
    'Marks':[89,90,np.nan,88]
}

df = pd.DataFrame(data)
print("\n Original Data:")
print(df)

# Numerical missing value fill 
print("\n Data After Filling Age.nan from mean of Age")
# df['Age'].fillna(df['Age'].mean(), inplace=True)  old way 
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

print("\n Data After Filling MArks.nan from mean of Marks")
df['Marks']= df['Marks'].fillna(df['Marks'].mean())
print(df)


#Categorial missing values fill
print("\n Data After Filling  Name")
df['Name'] = df['Name'].fillna("Unknown")
print(df)