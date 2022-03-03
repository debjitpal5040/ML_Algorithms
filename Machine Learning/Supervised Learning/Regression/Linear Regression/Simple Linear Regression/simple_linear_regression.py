# -*- coding: utf-8 -*-
"""Simple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zw6DcpTLAW35wxuEsLvNTTqMmJeUDM3i

# Simple Linear Regression

## Importing the necessary Libraries and Packages
"""

from sklearn.model_selection import train_test_split # splitting the dataset
from sklearn.linear_model import LinearRegression # regression algorithm
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_absolute_percentage_error # accuracy metric
import numpy as np # data processing
import pandas as pd # data processing 
import matplotlib.pyplot as plt # data plotting

"""## Importing the csv file as a DataFrame"""

df = pd.read_csv("Salary_Data.csv")
df.head()

"""## Now taking 2 parts from the dataset
### X : which contains only the <b>YearsExperience</b> column<br>y : which contains only the <b>Salary</b> column 
"""

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

"""## Visualization of the data"""

plt.figure(figsize=(6, 6), dpi=150)
plt.style.use('dark_background')
YearsExperience = df['YearsExperience']
Salary = df['Salary']
plt.scatter(YearsExperience,Salary)
plt.xticks(np.arange(1, 12, 1))
plt.yticks(np.arange(37000,128000,10000))
plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

"""## Split the <b>X</b> and <b>y</b> Dataframes for Test and Training"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)

"""## Implementation of the Model"""

reg=LinearRegression()
reg.fit(X_train,y_train)
y_pred = reg.predict(X_test)

"""## Performance of the Model"""

# Printing the coefficient of determination of the regression
print("The coefficient of determination :", r2_score(y_test,y_pred))

"""## Plotting the Regression

### Training Dataset
"""

plt.figure(figsize=(6, 6), dpi=150)
plt.style.use('dark_background')
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,reg.predict(X_train),color='blue')
plt.xticks(np.arange(1, 12, 1))
plt.yticks(np.arange(37000,128000,10000))
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

"""### Test Dataset"""

plt.figure(figsize=(6, 6), dpi=150)
plt.style.use('dark_background')
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, reg.predict(X_test), color = 'blue')
plt.xticks(np.arange(1, 12, 1))
plt.yticks(np.arange(37000,128000,10000))
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

"""## Additional Performance Metrics"""

print('Mean Absolute Error (MAE) :', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error (MSE) :', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error (RMSE) :', mean_squared_error(y_test, y_pred, squared=False))
print('Mean Absolute Percentage Error (MAPE) :', mean_absolute_percentage_error(y_test, y_pred))