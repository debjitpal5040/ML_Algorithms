# Support Vector Regression

In 𝜈-SVR, the parameter 𝜈 is used to determine the proportion of the number of support vectors you desire to keep in your solution with respect to the total number of samples in the dataset. In 𝜈-SVR the parameter 𝜖

is introduced into the optimization problem formulation and it is estimated automatically (optimally) for you.

However, in 𝜖
-SVR you have no control on how many data vectors from the dataset become support vectors, it could be a few, it could be many. Nonetheless, you will have total control of how much error you will allow your model to have, and anything beyond the specified 𝜖 will be penalized in proportion to 𝐶

, which is the regularization parameter.

Depending of what I want, I choose between the two. If I am really desperate for a small solution (fewer support vectors) I choose 𝜈
-SVR and hope to obtain a decent model. But if I really want to control the amount of error in my model and go for the best performance, I choose 𝜖-SVR and hope that the model is not too complex (lots of support vectors). 

Linear Support Vector Regression.

Similar to SVR with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.

This class supports both dense and sparse input.

Nu Support Vector Regression.

Similar to NuSVC, for regression, uses a parameter nu to control the number of support vectors. However, unlike NuSVC, where nu replaces C, here nu replaces the parameter epsilon of epsilon-SVR.

The implementation is based on libsvm.

Epsilon-Support Vector Regression.

The free parameters in the model are C and epsilon.

The implementation is based on libsvm. The fit time complexity is more than quadratic with the number of samples which makes it hard to scale to datasets with more than a couple of 10000 samples. For large datasets consider using LinearSVR or SGDRegressor instead, possibly after a Nystroem transformer.