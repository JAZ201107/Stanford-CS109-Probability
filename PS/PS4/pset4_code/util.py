"""
!!! DO NOT MODIFY THIS FILE !!!

You are welcome to read this file to see how the provided functions
are implemented, but you should not modify this file. Any modifications
made to this file will be ignored during autograding.

!!! DO NOT MODIFY THIS FILE !!!
"""

from random import sample

def make_word_list(filename):
    '''
    From a file name, return list of standardized words in the 
    file.
    '''
    all_words = []
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            line_words = line.split(' ')
            for word in line_words:
                word = standardize(word)
                if len(word) != 0: 
                    all_words.append(word)
    return all_words


def make_word_count_map(file_word_list):
    '''
    From a list of words in the file, count the number 
    of times each word occurs in that file. Return a dictionary 
    that maps words to the frequency with which they appear in 
    the document.
    '''
    counts = {}
    for word in file_word_list:
        counts[word] = counts.get(word, 0) + 1
    return counts


def standardize(word):
    '''
    Standardizes a word by making it lowercase and removing
    punctuation. 
    '''
    return word.lower().strip(" .,-;\n:'`;?")


EPSILON = 0.000001
def get_probability(word_prob_map, word):
    if word in word_prob_map:
        return word_prob_map[word]
    return EPSILON


def print_partial_dict(dictionary, message=''):
    '''
    Nothing interesting going on here from a probability standpoint.
    This function prints five randomly selected key-value pairs from a 
    provided dictionary. We opt to print a few values rather than print
    the entire dictionary since the probability and count maps are
    rather large.
    '''
    print(message)

    if len(dictionary) < 5:
        print(dictionary)
    else:
        data = sample(dictionary.items(), 5)
        print('{')
        for k, v in data:
            print(f'    {k}: {v}')
        print('    ... many more key-value pairs omitted ...')
        print('}')
