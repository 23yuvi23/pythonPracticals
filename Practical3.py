# Jo data numbers nahi, categories/text me hota hai = Categorial data 

import pandas as pd 

# sklearn = Machine Learning library
# preprocessing = data ko prepare karne wale tools
# LabelEncoder = ek tool jo text → number karta hai
from sklearn.preprocessing import LabelEncoder

data = {
    'Name' : ['Rahul', 'Amit', 'Aman','Ram'],
    'Gender':['Male' ,'Male' ,"Female","Male"]
}

df= pd.DataFrame(data)
print("Original Data" , df)

#encoding 
# Ek encoder object bana diya (jaise machine bana li)
le = LabelEncoder()

# df['Gender'] = Gender column uthaya (Male, Female)
# fit() = Unique values seekhta hai
# transform() = Unko numbers me convert karta hai
# fit_transform() = Shortcut = pehle seekh + phir convert
df['Gender'] = le.fit_transform(df['Gender'])

print("\nAfter Encoding")
print(df)