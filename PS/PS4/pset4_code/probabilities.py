"""
*************************IMPORTANT*************************
NOTE TO STUDENTS: You do NOT need to modify this file.
In fact, you don't really need to read this file at all,
but you can do so if you are curious.

You will call these functions in inferProbFlu().

Remember that you won't submit this file for autograding.
All of your work should go in the files listed for
submission on the assignment handout.
*************************IMPORTANT*************************
"""
def probStress():
  return 0.5

def probExposure():
  return 0.1

def probCold(s, e):
  if s == 0 and e == 0:
    return 0.01
  if s == 0 and e == 1:
    return 0.2
  if s == 1 and e == 0:
    return 0.3
  if s == 1 and e == 1:
    return 0.7
  raise IndexError("valid parameters are [0,1]")

def probFlu(s, e):
  if s == 0 and e == 0:
    return 0.01
  if s == 0 and e == 1:
    return 0.5
  if s == 1 and e == 0:
    return 0.1
  if s == 1 and e == 1:
    return 0.8
  raise IndexError("valid parameters are [0,1]")

_symptom_dict = {1: [0.03, 0.20, 0.80, 0.60],
                2: [0.05, 0.70, 0.60, 0.80],
                3: [0.03, 0.50, 0.50, 0.90],
                4: [0.02, 0.30, 0.90, 0.50],
                5: [0.01, 0.80, 0.80, 0.60]}

def probSymptom(i, f, c):
  bin_val = 2*f+c # decimal conversion of binary number fc
  return _symptom_dict[i][bin_val]

