# Model Building = data se prediction model banana
# Scikit-Learn =  Machine Learning models banane ke liye ready-made tools deta hai 
# Tu khud se formula likhne ki jagah, seedha library use karta hai.

import pandas as pd

# train_test_split =  Data ko 2 parts me todne ke liye 1-Train Data 2-Testing Data
from sklearn.model_selection import train_test_split
# LinearRegression = Model banane ke liye (prediction karega)
from sklearn.linear_model import LinearRegression

data = {
    'Hours':[1,2,3,4,5],
    'Marks':[35,50,65,70,85]
}

df= pd.DataFrame(data)
# print(df)

# input(X) and output(Y)
x= df[['Hours']]
y=df['Marks']

# Split data (training + testing)
x_train, x_test, y_train ,y_test = train_test_split(x,y, test_size=0.2)

# Model Create
model = LinearRegression()

# Train Model
model.fit(x_train,y_train)

# predict
prediction = model.predict([[6]])

print("Predicted Marks:", prediction)