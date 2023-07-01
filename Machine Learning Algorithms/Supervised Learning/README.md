# Supervised Learning
Supervised learning is the types of machine learning in which machines are trained using well "labelled" training data, and on basis of that data, machines predict the output. The labelled data means some input data is already tagged with the correct output.

In supervised learning, the training data provided to the machines work as the supervisor that teaches the machines to predict the output correctly. It applies the same concept as a student learns in the supervision of the teacher.

Supervised learning is a process of providing input data as well as correct output data to the machine learning model. The aim of a supervised learning algorithm is to find a mapping function to map the input variable(x) with the output variable(y).

In the real-world, supervised learning can be used for Risk Assessment, Image classification, Fraud Detection, spam filtering, etc. 

## How Supervised Learning Works
In supervised learning, models are trained using labelled dataset, where the model learns about each type of data. Once the training process is completed, the model is tested on the basis of test data (a subset of the training set), and then it predicts the output.

The working of Supervised learning can be easily understood by the below example and diagram:

<img width="693" alt="Screenshot 2021-11-13 at 13 48 43" src="https://user-images.githubusercontent.com/76846542/141611574-cfaa4d6c-8d8d-4f1f-8590-cda97c8920da.png">
Suppose we have a dataset of different types of shapes which includes square, rectangle, triangle, and Polygon. Now the first step is that we need to train the model for each shape.

    If the given shape has four sides, and all the sides are equal, then it will be labelled as a Square.
    If the given shape has three sides, then it will be labelled as a triangle.
    If the given shape has six equal sides then it will be labelled as hexagon.

Now, after training, we test our model using the test set, and the task of the model is to identify the shape.

The machine is already trained on all types of shapes, and when it finds a new shape, it classifies the shape on the bases of a number of sides, and predicts the output.

## Types of Supervised Learning Algorithm
Regression and Classification algorithms are both Supervised Learning algorithms. Both the algorithms are used for prediction in Machine learning and work with the labeled datasets. But the difference between both is how they are used for different machine learning problems.

<img width="427" alt="Screenshot 2021-11-13 at 13 47 06" src="https://user-images.githubusercontent.com/76846542/141611522-7ba0d150-4210-4fb2-8fae-92ebc62a3252.png">

The main difference between Regression and Classification algorithms that Regression algorithms are used to predict the <i>continuous</i> values such as price, salary, age etc. and Classification algorithms are used to predict/classify the <i>discrete</i> values such as Male or Female, True or False, Spam or Not Spam etc.

<img width="676" alt="Screenshot 2021-08-29 at 14 12 35" src="https://user-images.githubusercontent.com/76846542/131244378-9f8b039a-e77b-4aef-bd49-6c35ceaa2d6a.png">

## <u>Classification</u>


Classification is a process of finding a function which helps in dividing the dataset into classes based on different parameters. In Classification, a computer program is trained on the training dataset and based on that training, it categorizes the data into different classes.

The task of the classification algorithm is to find the mapping function to map the input(x) to the discrete output(y).

<b>Example : </b> The best example to understand the Classification problem is Email Spam Detection. The model is trained on the basis of millions of emails on different parameters, and whenever it receives a new email, it identifies whether the email is spam or not. If the email is spam, then it is moved to the Spam folder.

### <i>Types of Classification Algorithms</i>

Classification Algorithms can be further divided into the following types:

    Logistic Regression
    K-Nearest Neighbours
    Support Vector Machines
    Kernel SVM
    Naïve Bayes
    Decision Tree Classification
    Random Forest Classification

## <u>Regression</u>

Regression is a process of finding the correlations between dependent and independent variables. It helps in predicting the continuous variables such as prediction of Market Trends, prediction of House prices etc.

The task of the Regression algorithm is to find the mapping function to map the input variable(x) to the continuous output variable(y).

<b>Example : </b> Suppose we want to do weather forecasting, so for this, we will use the Regression algorithm. In weather prediction, the model is trained on the past data, and once the training is completed, it can easily predict the weather for future days.

### <i>Types of Regression Algorithms</i>

Regression Algorithms can be further divided into the following types:

    Simple Linear Regression
    Multiple Linear Regression
    Polynomial Regression
    Support Vector Regression
    Decision Tree Regression
    Random Forest Regression

## <u>Difference between Regression and Classification</u>
<img width="811" alt="Screenshot 2021-08-29 at 14 14 06" src="https://user-images.githubusercontent.com/76846542/131244419-3ccacd98-2081-4b14-81a9-deb2f99b9437.png">
