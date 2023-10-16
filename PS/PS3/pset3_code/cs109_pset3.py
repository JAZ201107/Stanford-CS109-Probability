# Name:
# Stanford email:

########### CS109 Problem Set 3, Question 1 ##############
"""
************************IMPORTANT************************
For all parts, do NOT modify the names of the functions.
Do not add or remove parameters to them either.
Moreover, make sure your return value is exactly as 
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. You
are free to write helper functions if you so desire.
Do NOT rename this file.
************************IMPORTANT************************
"""

# Do not add import statements.
# Do not remove this import statement either.
from numpy.random import rand

# part (a) - completed for you
def simulate_bernoulli(p=0.4):
    if rand() < p:
        return 1
    return 0


# part (b)
def simulate_binomial(n=20, p=0.4):
    pass  # TODO: delete this line and implement this function!


# part (c)
def simulate_geometric(p=0.03):
    pass  # TODO: delete this line and implement this function!


# part (d)
def simulate_neg_binomial(r=5, p=0.03):
    pass  # TODO: delete this line and implement this function!


# Note for parts (e) and (f):
# Since `lambda` is a reserved word in Python, we've used
# the variable name `lamb` instead. Do NOT use the word
# `lambda` in your code. It won't do what you want!


# part (e)
def simulate_poisson(lamb=3.1):
    pass  # TODO: delete this line and implement this function!


# part (f)
def simulate_exponential(lamb=3.1):
    pass  # TODO: delete this line and implement this function!


def main():
    """
    We've provided this for convenience.
    Feel free to modify this function however you like.
    We won't grade anything in this function.
    """
    print("Bernoulli:", simulate_bernoulli())


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
