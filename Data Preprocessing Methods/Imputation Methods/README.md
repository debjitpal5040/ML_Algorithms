# Imputation Methods


Imputation is a method used to fill in missing values in datasets. It is a crucial step in data preprocessing to ensure the quality and completeness of the data. Below are some common imputation methods:

## Mean Imputation

Mean imputation replaces missing values with the mean value of the entire feature column. This method is simple but can distort the data distribution.

```python
from sklearn.impute import SimpleImputer
import numpy as np

data = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = SimpleImputer(strategy='mean')
imputed_data = imputer.fit_transform(data)
```

## Median Imputation

Median imputation replaces missing values with the median value of the feature column. This method is more robust to outliers compared to mean imputation.

```python
from sklearn.impute import SimpleImputer
import numpy as np

data = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = SimpleImputer(strategy='median')
imputed_data = imputer.fit_transform(data)
```

## Mode Imputation

Mode imputation replaces missing values with the most frequent value (mode) of the feature column. This method is useful for categorical data.

```python
from sklearn.impute import SimpleImputer
import numpy as np

data = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = SimpleImputer(strategy='most_frequent')
imputed_data = imputer.fit_transform(data)
```

## K-Nearest Neighbors Imputation

K-Nearest Neighbors (KNN) imputation uses the k-nearest neighbors to estimate the missing values. This method can capture more complex relationships in the data.

```python
from sklearn.impute import KNNImputer
import numpy as np

data = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = KNNImputer(n_neighbors=2)
imputed_data = imputer.fit_transform(data)
```

## Conclusion

Choosing the right imputation method depends on the nature of your data and the specific requirements of your analysis. It is often useful to try multiple methods and compare their performance.
