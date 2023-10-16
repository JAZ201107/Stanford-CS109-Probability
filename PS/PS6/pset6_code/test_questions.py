# pylint: disable = C0330, missing-function-docstring, unused-argument, invalid-name
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
import questions

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='netflix',
    expected=0.49577777777777776,
)
def test_question_nb_a(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_nb_a
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='ancestry',
)
def test_question_nb_b(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_nb_b
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='ancestry',
)
def test_question_nb_c(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_nb_c
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=NaiveBayes,
    parameters={'use_mle': True},
    dataset_name='netflix',
)
def test_question_nb_d(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_nb_d
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
    expected=np.array([8, 11, 13, 16, 17]),
)
def test_question_lr_a(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_lr_a
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='heart',
)
def test_question_lr_b(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_lr_b
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

@utils.question_part(
    classifier=LogisticRegression,
    parameters={'learning_rate': 0.0001, 'max_steps': 10000},
    dataset_name='ancestry',
)
def test_question_lr_c(clf, train_features, train_labels, test_features, test_labels):
    f = questions.question_lr_c
    l = locals()
    return f(**{k: l[k] for k in set(f.__code__.co_varnames[:f.__code__.co_argcount])})

if __name__ == '__main__':
    utils.main(sys.argv[1:])
