# Multiple Linear Regression

In Simple Linear Regression, a single Independent/Predictor(X) variable is used to model the response variable (Y). But there may be various cases in which the response variable is affected by more than one predictor variable; for such cases, the Multiple Linear Regression algorithm is used.

Moreover, Multiple Linear Regression is an extension of Simple Linear regression as it takes more than one predictor variable to predict the response variable. We can define it as <i>"Multiple Linear Regression is one of the important regression algorithms which models the linear relationship between a single dependent continuous variable and more than one independent variable".</i>

<b>Example : </b> Prediction of CO<sub>2</sub> emission based on engine size and number of cylinders in a car.

### Some key points about MLR

1.  For MLR, the dependent or target variable(Y) must be the continuous/real, but the predictor or independent variable may be of continuous or categorical form.
2.  Each feature variable must model the linear relationship with the dependent variable.
3.  MLR tries to fit a regression line through a multidimensional space of data-points.
## MLR equation

In Multiple Linear Regression, the target variable(Y) is a linear combination of multiple predictor variables x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ...,x<sub>n</sub>. Since it is an enhancement of Simple Linear Regression, so the same is applied for the multiple linear regression equation, the equation becomes:

Y= b<sub>0</sub>+b<sub>1</sub>x<sub>1</sub>+ b<sub>2</sub>x<sub>2</sub>+ b<sub>3</sub>x<sub>3</sub>+...... b<sub>n</sub>x<sub>n</sub>      ............... (a)  

Y = Output/Response variable

b<sub>0</sub>, b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub> , b<sub>n</sub>.... = Coefficients of the model

x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>,... = Various Independent/feature variable

## Assumptions for Multiple Linear Regression

1. A linear relationship should exist between the Target and predictor variables.
The regression residuals must be normally distributed.
2. MLR assumes little or no multicollinearity (correlation between the independent variable) in data.