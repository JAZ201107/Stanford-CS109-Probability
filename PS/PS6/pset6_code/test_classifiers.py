# pylint: disable = missing-function-docstring
'''
Written by Tim Gianitsos

*************************IMPORTANT*************************
NOTE TO STUDENTS: You do NOT need to modify this file.
Remember that you won't submit this file for autograding.
All of your work should go in the files listed for
submission on the assignment handout.

For instructions on how to run the code in this file, see
the README file in the starter code.
*************************IMPORTANT*************************
'''

import sys

import numpy as np

import utils
from naive_bayes import NaiveBayes
from logistic_regression import LogisticRegression

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='simple',
    expected={0: 2, 1: 2},
    message='Outputs the label counts Naive Bayes learned from training'
)
def fit_bayes_label_count_simple(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, True)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='simple',
    expected={(0, 0, 0): 2, (1, 0, 0): 1, (1, 1, 0): 1, (0, 1, 1): 2, (1, 0, 1): 1, (1, 1, 1): 1},
    message='Outputs the feature counts Naive Bayes learned from training'
)
def fit_bayes_feature_count_simple(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, False)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='netflix',
    expected={0: 2269, 1: 2231},
    message='Outputs the label counts Naive Bayes learned from training'
)
def fit_bayes_label_count_netflix(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, True)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='netflix',
    expected={
        (0, 1, 1): 1497, (1, 1, 1): 1487, (2, 1, 1): 1325, (3, 1, 1): 1349, (4, 0, 1): 621,
        (5, 1, 1): 1354, (6, 1, 1): 1341, (7, 0, 1): 679, (8, 1, 1): 1922, (9, 0, 1): 762,
        (10, 1, 1): 1516, (11, 1, 1): 1476, (12, 1, 1): 1954, (13, 1, 1): 1498, (14, 1, 1): 1136,
        (15, 1, 1): 1151, (16, 0, 1): 558, (17, 0, 1): 649, (18, 0, 1): 563, (0, 0, 0): 940,
        (1, 0, 0): 718, (2, 0, 0): 736, (3, 0, 0): 779, (4, 0, 0): 981, (5, 1, 0): 1356,
        (6, 1, 0): 1412, (7, 1, 0): 1361, (8, 1, 0): 1957, (9, 0, 0): 688, (10, 1, 0): 1507,
        (11, 0, 0): 809, (12, 1, 0): 1987, (13, 1, 0): 1524, (14, 1, 0): 1286, (15, 1, 0): 1260,
        (16, 1, 0): 1726, (17, 1, 0): 1287, (18, 0, 0): 1560, (2, 0, 1): 906, (4, 1, 1): 1610,
        (5, 0, 1): 877, (6, 0, 1): 890, (9, 1, 1): 1469, (15, 0, 1): 1080, (18, 1, 1): 1668,
        (7, 1, 1): 1552, (16, 1, 1): 1673, (17, 1, 1): 1582, (3, 1, 0): 1490, (7, 0, 0): 908,
        (11, 1, 0): 1460, (18, 1, 0): 709, (1, 1, 0): 1551, (4, 1, 0): 1288, (5, 0, 0): 913,
        (6, 0, 0): 857, (9, 1, 0): 1581, (16, 0, 0): 543, (1, 0, 1): 744, (2, 1, 0): 1533,
        (13, 0, 0): 745, (11, 0, 1): 755, (13, 0, 1): 733, (15, 0, 0): 1009, (10, 0, 0): 762,
        (17, 0, 0): 982, (14, 0, 0): 983, (8, 0, 0): 312, (0, 1, 0): 1329, (0, 0, 1): 734,
        (3, 0, 1): 882, (10, 0, 1): 715, (14, 0, 1): 1095, (8, 0, 1): 309, (12, 0, 1): 277,
        (12, 0, 0): 282
    },
    message='Outputs the feature counts Naive Bayes learned from training'
)
def fit_bayes_feature_count_netflix(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, False)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='ancestry',
    message='Outputs the label counts Naive Bayes learned from training'
)
def fit_bayes_label_count_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, True)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='ancestry',
    message='Outputs the feature counts Naive Bayes learned from training'
)
def fit_bayes_feature_count_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, False)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='heart',
    message='Outputs the label counts Naive Bayes learned from training'
)
def fit_bayes_label_count_heart(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, True)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='heart',
    message='Outputs the feature counts Naive Bayes learned from training'
)
def fit_bayes_feature_count_heart(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels, False)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='simple',
    expected=np.array([-0.14577434, 0.82004294, -0.06660849]),
    message='Outputs the weights Logistic Regression learned from training'
)
def fit_logistic_simple(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 1500},
    dataset_name='netflix',
    expected=np.array([
        -1.21519064e+00,  1.43788786e-01, -3.55550372e-02, -1.96166019e-01,
        -1.14173764e-01,  3.25305312e-01,  3.00158721e-02, -1.13328595e-01,
        2.12799561e-01, -4.67992764e-02, -8.72192346e-02,  7.96961369e-02,
        4.61929225e-02,  9.40589329e-03, -1.68137265e-03, -1.08039126e-01,
        5.73541313e-03, -2.19154037e-02,  2.74605127e-01,  1.75370473e+00,
    ]),
    message='Outputs the weights Logistic Regression learned from training'
)
def fit_logistic_netflix(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='ancestry',
    message='Outputs the weights Logistic Regression learned from training'
)
def fit_logistic_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
    message='Outputs the weights Logistic Regression learned from training'
)
def fit_logistic_heart(clf, train_features, train_labels, test_features, test_labels):
    return fitting(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='simple',
    expected=1.0,
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': False},
    dataset_name='simple',
    expected=1.0,
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_map_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': False},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_map_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': False},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_map_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_mle_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': False},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_bayes_map_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='simple',
    expected=1.0,
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_simple(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 1500},
    dataset_name='netflix',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_netflix(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='ancestry',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_ancestry(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
    message='Percentage of correctly labeled answers:'
)
def predict_logistic_heart(clf, train_features, train_labels, test_features, test_labels):
    return predictions(clf, train_features, train_labels, test_features, test_labels)

#pylint:disable=unused-argument
def fitting(clf, train_features, train_labels, test_features, test_labels, use_nb_labels=None):
    clf.fit(train_features, train_labels)
    return (
        clf.label_counts if use_nb_labels is True
        else clf.feature_counts if use_nb_labels is False
        else clf.weights
    )

def predictions(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    result_labels = clf.predict(test_features)
    assert len(test_labels) == len(result_labels)
    return (test_labels == result_labels).sum() / len(test_labels)
#pylint:enable=unused-argument

if __name__ == '__main__':
    utils.main(sys.argv[1:])
