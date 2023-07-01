# Linear Regression

Linear regression is a statistical method that allows us to model the relationship between a dependent variable and one or more independent variables. It is one of the most widely used techniques in data analysis and machine learning, as it can help us understand how different factors affect an outcome of interest, and make predictions based on the observed data.

Here we will introduce the basic concepts of linear regression, such as the equation of the regression line, the coefficient of determination, and the assumptions of the linear model. We will also show how to perform linear regression in Python using the scikit-learn library, and how to interpret the results and evaluate the model performance.

The equation of the regression line

The simplest form of linear regression is called simple linear regression, which involves only one independent variable (x) and one dependent variable (y). The goal of simple linear regression is to find a straight line that best fits the data points, such that the sum of squared errors (SSE) between the observed values of y and the predicted values of y is minimized. The equation of this line can be written as:

y = b0 + b1 * x

where b0 is the intercept (the value of y when x is zero), and b1 is the slope (the change in y for a unit change in x). These are called the parameters or coefficients of the regression model, and they can be estimated from the data using various methods, such as ordinary least squares (OLS).

The coefficient of determination

One way to measure how well the regression line fits the data is to use the coefficient of determination, also known as R-squared. This is a value between 0 and 1 that indicates the proportion of variance in y that is explained by x. A higher R-squared means that the model captures more of the variability in y, and a lower R-squared means that the model leaves more unexplained. The formula for R-squared is:

R-squared = 1 - SSE / SST

where SSE is the sum of squared errors between the observed and predicted values of y, and SST is the total sum of squares, which is the sum of squared deviations of y from its mean. R-squared can also be interpreted as the square of the correlation coefficient between x and y.

The assumptions of the linear model

Linear regression is based on some assumptions that need to be checked before applying it to real data. These are:

- Linearity: The relationship between x and y is linear, or can be approximated by a linear function.
- Independence: The errors (residuals) are independent from each other and from x.
- Homoscedasticity: The variance of the errors is constant across different values of x.
- Normality: The errors are normally distributed with mean zero and constant variance.

If these assumptions are violated, then the results of linear regression may be biased, inconsistent, or inefficient. Therefore, it is important to perform some diagnostic tests and plots to check for potential problems, such as outliers, multicollinearity, heteroscedasticity, or non-normality.
