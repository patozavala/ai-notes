""" 
Machine learning supervised algorithms
Author: Patricio Zavala (pazavala@uc.cl)
"""

import numpy as np 
# x [n,m]
#         y [n,1]
#         w [m,1]
class MachineLearner():
    def linear_regression(self, dataset):
        """
        Linear regression fits a model with coefficients w = (w1, ..., wp) to
        minimize the sum of squares error between an input observed dataset 
        and the predictions made by the linear approximation.

        Assumptions: 
            There is a linear relationship between the dependent variables 
            and the independent variables.

            All explanatory variables must be linearly independent.
            
            Observations are selected independently and randomly from the
            population.

        Args:
            dataset ([list]): list with an observed dataset.

        Returns:
            w ([numpy.ndarray]): coefficients.
        """

        x,y = dataset
        # solution (explain how to achieve this analitical expression)
        w = np.dot(np.linalg.inv(np.dot(x.T,x)), np.dot(x.T,y))
        return w

    def logistic_regression(self):
        """
        logistic regression algorithm for classification
        """
        pass
    def naive_bayes(self):
        pass
    def k_nearest_neighbors(self):
        pass
    def deceision_tree(self):
        pass
    def random_forest(self):
        pass

x = np.array([[1,1,1,1,1],[1,2,3,4,5]]).T
y = np.array([2,3,5,6,5])
y = np.reshape(y, [len(y),1])

dataset = [x,y]

ml = MachineLearner()

print(ml.linear_regression(dataset))