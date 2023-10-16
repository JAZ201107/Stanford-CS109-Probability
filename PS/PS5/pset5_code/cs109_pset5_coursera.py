# Do NOT add any other import statements.
import numpy as np
import copy
from cs109_pset5_util import get_filepath

# Name:
# Stanford email:


"""
Assembled by Lisa Yan and CS109 TA Anand Shankar
*************************IMPORTANT*************************
For the functions that we ask you to write, do NOT modify 
the name of the functions. Do not add or remove parameters to 
them either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""

def diff_sample_means(filepath):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.
    
    You can use the helper function get_filepath()
    defined in util.py.

    Return the difference in sample means (float) as 
    described in the handout.
    """
    pass  # TODO: delete this line and implement the function.


def estimate_p_val(filepath, seed=109):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.

    Return the p-value (float) as described in the handout.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###

    # TODO: write some awesome code here.

    ### END YOUR CODE FOR PART (B) ###


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    filepath = get_filepath('learningOutcomes.csv')
    
    print(f"Calling diff_sample_means with {filepath}:")
    print("\tReturn value was:", diff_sample_means(filepath))

    print(f"Calling estimate_p_val with {filepath}:")
    print("\tReturn value was:", estimate_p_val(filepath))

    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
