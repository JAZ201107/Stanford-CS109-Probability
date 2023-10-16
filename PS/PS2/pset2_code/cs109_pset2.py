# Do NOT add any other import statements
import numpy as np

# Name:
# Stanford email:

"""
************************IMPORTANT************************
For calculate_probs and calculate_cond_probs, do NOT 
modify the name of the functions. Do not add or remove 
parameters to them either. Moreover, make sure your 
return value is exactly as described in the PDF handout 
and in the provided function comments. Remember that your 
code is being autograded. You are free to write helper 
functions if you so desire. Do NOT rename this file.
************************IMPORTANT************************
"""

def calculate_probs(filename):
    """
    filename is a path to a csv file, e.g. "bats.csv".
    You must use the filename variable. Do NOT alter the 
    filename variable, and do NOT hard-code a filepath;
    if you do, you'll likely fail the autograder.

    You should return a numpy array of length 6, 
    call it probs. probs[i] should be P(G_i) for 
    0 <= i <= 4. probs[5] should be P(T).

    See the assignment handout for some advice on how 
    to use numpy to make your life easier in this 
    function.
    """
    pass  # TODO: delete this line and implement the function


def calculate_cond_probs(filename):
    """
    filename is a path to a csv file, e.g. "bats.csv".
    As in calculate_probs, you must use this variable or you'll
    likely fail the autograder.

    You should return a numpy array of length 5, call it 
    probs, where probs[i] is equal to P(T | G_i). See 
    the assignment handout for some information on 
    numpy functionality that'll help you here.
    """
    pass  # TODO: delete this line and implement the function


def sandbox():
    """
    We won't autograde anything you write in this function.
    You should submit your answer to part (c) in the PDF
    you upload to Gradescope. But we've included this function
    here for convenience. It will get called by our provided
    main method. Feel free to do whatever you want here, 
    including leaving this function blank. We won't read it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call the 
    functions above. Feel free to modify this function however 
    you like. We won't grade anything in this function.
    """
    filename = 'bats.csv'

    print("****** Calling calculate_probs on 'bats.csv' *******")
    probs = calculate_probs(filename)
    print(f"\treturned {probs}")
    print("*********************************************\n")

    print("*** Beginning calculate_cond_probs on 'bats.csv' ***")
    cond_probs = calculate_cond_probs(filename)
    print(f"\treturned {cond_probs}")
    print("*********************************************\n")

    print("*** Beginning sandbox - convenience function ***")
    sandbox()
    print("*********************************************\n")


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
