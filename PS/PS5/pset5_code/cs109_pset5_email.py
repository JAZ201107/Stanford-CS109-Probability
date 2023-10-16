# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
from cs109_pset5_util import get_filepath

# Name:
# Stanford email:

"""
Assembled by Lisa Yan and CS109 TA Anand Shankar
*************************IMPORTANT*************************
For the functions we ask you to write, do NOT modify the name  
of the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def get_expectation(filepath):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X] (which is of type float).
    """
    pass  # TODO: delete this line and implement the function!


def get_squared_expectation(filepath):
    """
    filepath is the path to a data file.
    You must use the filepath variable. Do NOT 
    alter the filepath variable, and do NOT 
    hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X^2] (which is of type float).
    """
    pass  # TODO: delete this line and implement the function!


def optional_function():
    """
    We won't grade anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass  # TODO: delete this line and optionally implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    a_path = get_filepath('personKeyTimingA.txt')
    b_path = get_filepath('personKeyTimingB.txt')

    print(f"Calling get_expectation with {a_path}")
    print("\tReturn value was:", get_expectation(a_path))

    print(f"Calling get_expectation with {b_path}")
    print("\tReturn value was:", get_expectation(b_path))

    print(f"Calling get_squared_expectation with {a_path}")
    print("\tReturn value was:", get_squared_expectation(a_path))

    print(f"Calling get_squared_expectation with {b_path}")
    print("\tReturn value was:", get_squared_expectation(b_path))

    print("Calling optional_function")
    print("\tReturn value was:", optional_function())

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
