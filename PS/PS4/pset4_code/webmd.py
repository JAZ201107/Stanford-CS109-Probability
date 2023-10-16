# Name:
# Stanford email:

# Do NOT add any other import statements.
import numpy as np

from probabilities import *

"""
*************************IMPORTANT*************************
The file probabilities contains helper functions 
probStress(), probExposure(), probCold(s, e), probFlu(s, e), 
and probSymptom(i, f, c). You should NOT re-implement these
functions; they are imported for you already.

We may additionally test your code with different values
from what is provided to you.

You can call the functions directly from this file:
  x = probFlu() + 5     # not a probability

*************************IMPORTANT*************************
"""


def inferProbFlu(ntrials = 1000000) -> float:
    """    
    Computes P(Flu = 1 | Exposure = 1, X_2 = 1), the probability
    of flu conditioned on observing that the patient has had
    exposure to a sick friend and that they are experiencing
    Symptom 2 (runny nose). Uses rejection sampling.
    :param ntrials: the number of observations to sample.
    """
    return -1 # TODO: delete this line and implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("Calling inferProbFlu():")
    print("\tReturn value was:", inferProbFlu())
    print("Done!")


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()

