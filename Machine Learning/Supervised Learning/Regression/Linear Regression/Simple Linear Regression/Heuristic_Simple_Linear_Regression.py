import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.markers import MarkerStyle

# read the csv file
df = pd.read_csv('Machine Learning/Supervised Learning/Regression/Linear Regression/Simple Linear Regression/Salary_Data.csv')
x = df['YearsExperience'].tolist()  # x axis values
y = df['Salary'].tolist()  # y axis values
xy = [x[i]*y[i] for i in range(len(x))]  # multiplying x and y values
x2 = [x[i]**2 for i in range(len(x))]  # squaring x values
X = sum(x)  # sum of x values
Y = sum(y)  # sum of y values
X2 = sum(x2)  # sum of x2 values
XY = sum(xy)  # sum of xy values
n = len(x)  # number of values
A = [[n, X], [X, X2]]  # matrix A
B = [Y, XY]  # matrix B
A = np.array(A)  # converting to numpy array
B = np.array(B)  # converting to numpy array
A_inv = np.linalg.inv(A)  # inverse of A
ans = np.matmul(A_inv, B)  # multiplying A inverse and B
a = ans[0]  # a value
b = ans[1]  # b value
plt.style.use('dark_background')  # changing the background color
plt.scatter(x, y, marker=MarkerStyle('.'), color='red')  # plotting points
plt.xticks(np.arange(1, 12, 1))  # setting x axis values
plt.yticks(np.arange(37000, 128000, 10000))  # setting y axis values
plt.xlabel('Years of Experience')  # setting x label
plt.ylabel('Salary')  # setting y label
plt.title('2D Scatter plot with best fit line')  # setting title
p = np.linspace(0, 11, 100)  # creating a list of 100 values
q = b*p+a  # equation of line
plt.plot(p, q, color='blue')  # plotting line
plt.savefig('Machine Learning/Supervised Learning/Regression/Linear Regression/Simple Linear Regression/Images/Heuristic_Simple_Linear_Regression.png', bbox_inches='tight', dpi=150)  # saving the plot
plt.show()  # showing the graph