# Linear Regression

Linear regression is one of the easiest and most popular Machine Learning algorithms. It is a statistical method that is used for predictive analysis. Linear regression makes predictions for continuous/real or numeric variables such as sales, salary, age, product price, etc.

Linear regression algorithm shows a linear relationship between a dependent (y) and one or more independent (y) variables, hence called as linear regression. Since linear regression shows the linear relationship, which means it finds how the value of the dependent variable is changing according to the value of the independent variable.

The linear regression model provides a sloped straight line representing the relationship between the variables.

<img width="429" alt="Screenshot 2021-08-29 at 14 40 43" src="https://user-images.githubusercontent.com/76846542/131245142-d4b91855-bf24-4d3c-8b24-495a83f6054d.png">

Mathematically, we can represent a linear regression as<br>
<img width="156" alt="Screenshot 2021-08-29 at 14 45 28" src="https://user-images.githubusercontent.com/76846542/131245277-8fb5d6a7-9c81-4a9f-89f6-f8f0adc3a47f.png">

Y = Dependent Variable (Target Variable)<br>
X = Independent Variable (predictor Variable)<br>
a<sub>0</sub> = Intercept of the line (Gives an additional degree of freedom)<br>
a<sub>1</sub> = Linear regression coefficient (scale factor to each input value)<br>
ε = Random error

The values for x and y variables are training datasets for Linear Regression model representation
## Types of Linear Regression

Linear regression can be further divided into two types of the algorithms.

### Simple Linear Regression
If a single independent variable is used to predict the value of a numerical dependent variable, then such a Linear Regression algorithm is called Simple Linear Regression.<br>
Notebook link : https://colab.research.google.com/drive/1zw6DcpTLAW35wxuEsLvNTTqMmJeUDM3i?usp=sharing
### Multiple Linear regression
If more than one independent variable is used to predict the value of a numerical dependent variable, then such a Linear Regression algorithm is called Multiple Linear Regression.
<br> Notebook link : https://colab.research.google.com/drive/1JGhK375g4sQG7aLfd3aN_M3zuaPlIBP0?usp=sharing <br>
## Finding the best fit line

When working with linear regression, our main goal is to find the best fit line that means the error between predicted values and actual values should be minimized. The best fit line will have the least error.

The different values for weights or the coefficient of lines (a<sub>0</sub>, a<sub>1</sub>) gives a different line of regression, so we need to calculate the best values for a0 and a1 to find the best fit line, so to calculate this we use cost function.

## Cost function

1. The different values for weights or coefficient of lines (a<sub>0</sub>, a<sub>1</sub>) gives the different line of regression, and the cost function is used to estimate the values of the coefficient for the best fit line.
2. Cost function optimizes the regression coefficients or weights. It measures how a linear regression model is performing.
3. We can use the cost function to find the accuracy of the <b>mapping function</b>, which maps the input variable to the output variable. This mapping function is also known as <b>Hypothesis function</b>.

For Linear Regression, we use the <b>Mean Squared Error (MSE)</b> cost function, which is the average of squared error occurred between the predicted values and actual values. It can be written as:

For the above linear equation, MSE can be calculated as:

<img width="277" alt="Screenshot 2021-08-29 at 17 21 12" src="https://user-images.githubusercontent.com/76846542/131249384-5b67e903-fac6-49df-b4c3-6ea783625945.png">



N = Total number of observation <br>
Y<sub>i</sub> = Actual value <br>
(a<sub>1</sub>x<sub>i</sub>+a<sub>0</sub>) = Predicted value.

<b>Residuals:</b> The distance between the actual value and predicted values is called residual. If the observed points are far from the regression line, then the residual will be high, and so cost function will high. If the scatter points are close to the regression line, then the residual will be small and hence the cost function.

## Gradient Descent

1. Gradient descent is used to minimize the MSE by calculating the gradient of the cost function.
2. A regression model uses gradient descent to update the coefficients of the line by reducing the cost function.
3. It is done by a random selection of values of coefficient and then iteratively update the values to reach the minimum cost function.
## Model Performance

The Goodness of fit determines how the line of regression fits the set of observations. The process of finding the best model out of various models is called <b>optimization</b>. It can be achieved by below method:

 <b>R-squared method</b>

1. R-squared is a statistical method that determines the goodness of fit.
2. It measures the strength of the relationship between the dependent and independent variables on a scale of 0-100%.
3. The high value of R-square determines the less difference between the predicted values and actual values and hence represents a good model.
4. It is also called a <b>coefficient of determination</b>, or <b>coefficient of multiple determination</b> for multiple regression.
5. It can be calculated from the below formula:
<img width="246" alt="Screenshot 2021-08-29 at 17 22 07" src="https://user-images.githubusercontent.com/76846542/131249410-cd03d164-cc45-47a7-b70b-58384f5963cb.png">

## Assumptions of Linear Regression

Below are some important assumptions of Linear Regression. These are some formal checks while building a Linear Regression model, which ensures to get the best possible result from the given dataset.

### Linear relationship between the features and target
Linear regression assumes the linear relationship between the dependent and independent variables.
### Small or no multicollinearity between the features
Multicollinearity means high-correlation between the independent variables. Due to multicollinearity, it may difficult to find the true relationship between the predictors and target variables. Or we can say, it is difficult to determine which predictor variable is affecting the target variable and which is not. So, the model assumes either little or no multicollinearity between the features or independent variables.
### Homoscedasticity Assumption
Homoscedasticity is a situation when the error term is the same for all the values of independent variables. With homoscedasticity, there should be no clear pattern distribution of data in the scatter plot.
### Normal distribution of error terms
Linear regression assumes that the error term should follow the normal distribution pattern. If error terms are not normally distributed, then confidence intervals will become either too wide or too narrow, which may cause difficulties in finding coefficients.
It can be checked using the <b>q-q</b> plot. If the plot shows a straight line without any deviation, which means the error is normally distributed.
### No autocorrelations
The linear regression model assumes no autocorrelation in error terms. If there will be any correlation in the error term, then it will drastically reduce the accuracy of the model. Autocorrelation usually occurs if there is a dependency between residual errors.
