# Adaptive Boosting

AdaBoost, short for Adaptive Boosting, is a powerful ensemble learning technique used for both classification and regression tasks. Unlike bagging or voting, which focus on reducing variance, AdaBoost takes an adaptive approach to improve the overall accuracy by focusing on training examples that previous models struggled with.

**The Core Idea of AdaBoost:**

1. **Initial Weights:**
    - AdaBoost assigns equal weights to all data points in the training set.

2. **Train Weak Learner:**
    - A weak learner (often a simple decision tree) is trained on the entire data set.

3. **Calculate Error:**
    - The error rate of the weak learner is calculated. This represents the proportion of data points it misclassified (classification) or the average difference between its predictions and the actual target values (regression).

4. **Adjust Weights:**
    - The weights of data points that the weak learner misclassified are **increased**. This ensures these "difficult" examples get more focus in subsequent rounds. Conversely, weights of correctly classified points are decreased.

5. **Repeat Steps 2-4:**
    - The process repeats for multiple rounds, each time training a new weak learner on the adjusted weight distribution. Subsequent learners focus on the data points that prior models had difficulty with.

6. **Final Prediction:**
    - **Classification:** AdaBoost uses a weighted majority vote to make the final prediction. Each weak learner's vote is weighted by its accuracy in its corresponding round.
    - **Regression:** The final prediction is a weighted average of the predictions from all weak learners, with weights based on their accuracy.

**Impact on Predictions:**

- AdaBoost iteratively improves the performance by focusing on previously misclassified examples.
- The final model is a combination of multiple weak learners, each contributing based on its expertise in handling specific data points.

**Benefits of AdaBoost:**

- Can significantly improve the accuracy of models, especially for complex problems.
- Relatively robust to outliers as it downweights them in subsequent iterations.

**Things to Consider:**

- Can be sensitive to noisy data as upweighting errors can amplify their impact.
- May require careful selection of the number of weak learners to avoid overfitting.
- Can be computationally expensive compared to bagging or voting due to the multiple training rounds.

In conclusion, AdaBoost is a powerful ensemble learning technique that leverages a staged approach to improve model performance. By focusing on challenging data points in each iteration, it builds a robust model that combines the strengths of multiple weak learners in both classification and regression tasks.
