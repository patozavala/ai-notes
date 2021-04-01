""" 
Aritificial intelligence algorithms

Basic implementation of logistic regression and support vector machine 
algorithms.

Author: Patricio Zavala - pazavala@uc.cl
"""

import numpy as np 
import matplotlib.pyplot as plt 

# sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.datasets import make_blobs

def logistic_regression(x_train,y_train,x_test):
    """Logistic regression algorithm for prediction
    Args:
        x_train ([2D array]): data for training
        y_train ([1D array]): predictions for training
        x_test ([2D array]): data to make the prediction
    """
    regression = LogisticRegression()
    # training
    regression.fit(x_train,y_train)
    # prediction
    prediction = regression.predict(x_test)
    return prediction

def support_vector_machine():
    """
    Implementation a class example in which a data set randomly 
    generated was classified in two clusters.
    """
    # Generate isotropic Gaussian blobs for clustering
    X, y = make_blobs(n_samples=100, centers=2, random_state=6)

    classifier = svm.SVC(kernel='linear', C=1000)
    classifier.fit(X, y)

    # plot the decision function
    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = classifier.decision_function(xy).reshape(XX.shape)
    ax.contour(XX, YY, Z, colors='g', levels=[-1, 0, 1], alpha=0.5,
                linestyles=['-.','-','-.'])
    # plot support vectors
    ax.scatter(classifier.support_vectors_[:,0], 
               classifier.support_vectors_[:, 1], 
               s=100, linewidth=1,
               facecolors='none')
    plt.savefig('svm.png', metadata=None)
    plt.show()

if __name__ == '__main__':
    run_logistic_regression = False
    run_support_vector_machine = False

    if run_logistic_regression:
        # definition of a training dataset
        x_train = np.array([i*0.25 for i in range(2,22)]).reshape(-1,1)
        y_train = np.array([0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1])
        # data to make the prediction
        x_test = np.array([i for i in range(1,7)]).reshape(-1,1)
        print(logistic_regression(x_train, y_train, x_test))

    if run_support_vector_machine:
        support_vector_machine()
