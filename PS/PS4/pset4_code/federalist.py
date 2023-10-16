# Do NOT add or remove any other import statements
import collections
from numpy import log

from util import *

# Name:
# SUNet ID: 

"""
************************IMPORTANT************************
For functions we ask you to write, do NOT 
modify the name of the functions. Do not add or remove 
parameters to them either. Moreover, make sure your 
return value is exactly as described in the PDF handout 
and in the provided function comments. Remember that your 
code is being autograded. You are free to write helper 
functions if you so desire. Do NOT rename this file.
************************IMPORTANT************************
"""

def make_word_prob_map(word_list):
    """
    From a given list of words, approximate the 
    probability of a word being generated from the same 
    distribution as the file. Assume that each word is 
    produced independently, regardless of order.
    Return a dictionary that maps words to their 
    probabilities of appearing in the document.
    """
    ## BEGIN YOUR CODE
    return {}  # TODO: delete this line and implement the function
    ## END YOUR CODE


def calculate_doc_log_prob(author_word_prob_map, unknown_word_count_map):
    '''
    author_word_prob_map is a dictionary that maps words to the
    probability that the underlying (known) author wrote them.

    unknown_word_count_map is a dictionary that maps words in a
    document whose author is unknown to the number of times they 
    appeared in the document.

    Return a quantity proportional to the probability of the 
    unknown document given the known author. 
    '''
    ## BEGIN YOUR CODE
    return 1.0  # TODO: delete this line and implement the function
    ## END YOUR CODE


def determine_author(word_list1, author1, word_list2, author2,
                     unknown_word_list):
    '''
    word_list1 is a list of words in a document written by author1.
    word_list2 is a list of words in a document written by author2.
    unknown_word_list is a list of words in a document whose author is
    unknown.

    Return author1 if it's more likely that they wrote the unknown document.
    Otherwise, return author2.
    '''
    ## BEGIN YOUR CODE
    return author1  # TODO: delete this line and implement the function
    ## END YOUR CODE


def main():
    '''
    We provide this function for your convenience, simply to call
    the functions that we've asked you to write. Feel free to change
    the main function however you like. We won't grade anything
    in the main function.
    '''
    hamilton_words = make_word_list('hamilton.txt')
    madison_words = make_word_list('madison.txt')
    unknown_words = make_word_list('unknown.txt')

    hamilton_probs = make_word_prob_map(hamilton_words)
    madison_probs = make_word_prob_map(madison_words)
    print_partial_dict(hamilton_probs, 'Partial Hamilton Word Prob Map:')
    print_partial_dict(madison_probs, 'Partial Madison Word Prob Map:')

    unknown_counts = make_word_count_map(unknown_words)
    print_partial_dict(unknown_counts, 'Partial Unknown Doc Count Map:')    

    log_prob_unk_ham = calculate_doc_log_prob(hamilton_probs, unknown_counts)
    log_prob_unk_mad = calculate_doc_log_prob(madison_probs, unknown_counts)
    print('Log prob that Hamilton wrote unknown doc:', log_prob_unk_ham)
    print('Log prob that Madison wrote unknown doc:', log_prob_unk_mad)

    # Putting it all together 
    unknown_author = determine_author(hamilton_words, 'Alexander Hamilton',
                                      madison_words, 'James Madison',
                                      unknown_words)
    print('Unknown doc was probably written by:', unknown_author)


# This if-test is True if this file was executed directly on the 
# command line. It's False if this file was executed indirectly,
# e.g. as part of an import statement.
if __name__ == '__main__':
    main()

