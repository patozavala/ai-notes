# Support Vector Machines:
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

## The advantages of support vector machines are:

- SVMs are effective in high dimensional spaces.

- SVMs are still effective in cases where number of dimensions is greater than the number of samples.

- SVMs uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

- SVMs are versatile because different Kernel functions can be specified for the decision function.

## The disadvantages of support vector machines include:

- If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

- SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation.

## References
- https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-py

- https://scikit-learn.org/stable/modules/svm.html#svm