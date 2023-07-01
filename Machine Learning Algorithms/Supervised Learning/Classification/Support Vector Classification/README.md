# Support Vector Classification

You can select what to used based on your goal and what kind of data you have.

    If you have a classification problem, i.e., discrete label to predict, you can use C-classification and nu-classification.

    If you have a regression problem, i.e., continuous number to predict, you can use eps-regression and nu-regression.

    If you only have one class of the data, i.e., normal behavior, and want to detect outliers. one-classification.
Details

C-classification and nu-classification is for binary classification usage. Say if you want to build a model to classify cat vs. dog based on features for animals, i.e., prediction target is a discrete variable/label.

For details about difference between C-classification and nu-classification. You can find in the FAQ from LIBSVM

    Q: What is the difference between nu-SVC and C-SVC?

    Basically they are the same thing but with different parameters. The range of C is from zero to infinity but nu is always between [0,1]. A nice property of nu is that it is related to the ratio of support vectors and the ratio of the training error.

One-classification is for "outlier detection", where you only have one classes data. For example, you want to detect "unusual" behaviors of one user's account. But you do not have "unusual behavior" to train the model. But only the normal behavior.

eps-regression and nu-regression are used for regression problems, where you want to predict a continuous number say housing price. Detailed difference can be found here: Difference between ep-SVR and nu-SVR (and least squares SVR)

Linear Support Vector Classification.

Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples. This class supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.

Nu-Support Vector Classification.

Similar to SVC but uses a parameter to control the number of support vectors. The implementation is based on libsvm.
nu (float, default=0.5) = An upper bound on the fraction of margin errors (see User Guide) and a lower bound of the fraction of support vectors. Should be in the interval (0, 1].

C-Support Vector Classification.

The implementation is based on libsvm. The fit time scales at least quadratically with the number of samples and may be impractical beyond tens of thousands of samples. For large datasets consider using LinearSVC or SGDClassifier instead, possibly after a Nystroem transformer.