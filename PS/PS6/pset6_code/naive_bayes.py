'''
Naive Bayes Classifier
'''
import math
import numpy as np

"""
Starter Code for CS 109 Problem Set 6
Written by Tim Gianitsos

*************************IMPORTANT*************************
Do NOT modify the name of any functions. Do not add or remove
parameters to them either. Moreover, make sure your return
value is exactly as described in the PDF handout and in the
provided function comments. Remember that your code is being
autograded. You are free to write helper functions if you so
desire but they are not necessary. Do NOT rename this file.
Do NOT modify any code outside the begin and end code markers.
*************************IMPORTANT*************************
"""

class NaiveBayes:
    '''
    Naive Bayes Classifier

    For a datapoint, the Naive Bayes classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training,
    it learns probabilities by counting the occurences of feature/label combinations
    that it finds in the training data. During prediction, it uses these counts to
    compute probabilities.
    '''

    def __init__(self, use_mle):
        '''DO NOT RENAME INSTANCE VARIABLES'''
        self.label_counts = {}
        self.feature_counts = {}
        self.use_mle = use_mle # True for MLE, False for MAP with Laplace add-one smoothing

    def fit(self, train_features, train_labels):
        self.label_counts[0] = 0
        self.label_counts[1] = 0

        ### YOUR CODE HERE (~5-10 Lines)

        ### END YOUR CODE

    def predict(self, test_features):
        preds = np.zeros(test_features.shape[0], dtype=np.uint8)

        ### YOUR CODE HERE (~10-30 Lines)

        ### END YOUR CODE

        return preds
