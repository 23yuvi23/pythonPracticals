#Linear Regression is a statistical method used to find the relationship 
#between independent and dependent variables and to predict continuous 
#values.

# Scikit-Learn =  Machine Learning ka ready-made toolkit hai

# Model banana = model = LinearRegression()
# Train karna = model.fit(X, y)
# Predict karna = model.predict([[6]])

import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset 
data = {
    'Hours' : [1,2,3,4,5],
    'Marks' : [35,50,65,70,85]
}

df = pd.DataFrame(data)
# print(df)

# Input (X) and Output (y)
# Model ko input 2D me chahiye hota hai thats why [[]] in Hours
x=df[['Hours']]
y=df['Marks']

# Create model
model = LinearRegression()

#TrainModel
# in prac 9 diff output because 
# train_test_split(X, y, test_size=0.2)  = Random split 
model.fit(x,y)  # but poora data use ho raha hai yaha 

#predict 
prediction = model.predict([[6]])
print("Predicted Data is ", prediction)
