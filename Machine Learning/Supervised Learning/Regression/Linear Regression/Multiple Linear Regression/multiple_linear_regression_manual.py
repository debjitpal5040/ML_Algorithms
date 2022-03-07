import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
df = pd.read_csv('Machine Learning/Supervised Learning/Regression/Linear Regression/Multiple Linear Regression/Dataset/Startups.csv') # read the csv file
x=df['Research'].tolist() #x axis values
y=df['Marketing'].tolist() #y axis values
z=df['Profit'].tolist() #z axis values
x2=[x[i]**2 for i in range(len(x))] #squaring x values
y2=[y[i]**2 for i in range(len(y))] #squaring y values
xy=[x[i]*y[i] for i in range(len(x))] #multiplying x and y values
xz=[x[i]*z[i] for i in range(len(x))] #multiplying x and z values
yz=[y[i]*z[i] for i in range(len(y))] #multiplying y and z values
X=sum(x) #sum of x values
Y=sum(y) #sum of y values
Z=sum(z) #sum of z values
XY=sum(xy) #sum of xy values
XZ=sum(xz) #sum of xz values
YZ=sum(yz) #sum of yz values
X2=sum(x2) #sum of x2 values
Y2=sum(y2) #sum of y2 values
n=len(x) #number of values
A=[[n,X,Y],[X,X2,XY],[Y,XY,Y2]] #matrix A
B=[Z,XZ,YZ] #matrix B
A_inv = np.linalg.inv(A) #inverse of A
ans = np.matmul(A_inv,B) #multiplying A inverse and B
a=ans[0] #a value
b=ans[1] #b value
c=ans[2] #c value
plt.style.use('dark_background') #changing the background color
ax = plt.axes(projection ='3d') # syntax for 3-D projection
ax.scatter3D(x,y,z,marker=".", color="red") #plotting points
ax.set_xticks(np.arange(15000, 200000, 25000))
ax.set_yticks(np.arange(25000, 475000, 50000))
ax.set_zticks(np.arange(60000,220000,20000))
ax.set_xlabel('Research')
ax.set_ylabel('Marketing')
ax.set_zlabel('Profit')
plt.title('3D Scatter Plot with best fit plane')
p=np.linspace(15000,200000,100) #creating a list of 100 values
q=np.linspace(25000,475000,100) #creating a list of 100 values
p,q = np.meshgrid(p,q) #creating a meshgrid
eq = a+b*p+c*q #equation of plane
ax.plot_surface(p, q, eq, alpha=0.3,color="blue") #plotting plane
plt.savefig("Machine Learning/Supervised Learning/Regression/Linear Regression/Multiple Linear Regression/Images/multiple_linear_regression_manual.png",bbox_inches='tight',dpi=150) #saving the plot
plt.show()
