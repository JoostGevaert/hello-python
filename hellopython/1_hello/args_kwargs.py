### Very basic Python ###
import os
import sys
import io
from pprint import pprint as pp

### *args & **kwargs tutorial |  Real Python ###
# This function can only add 2 values
def my_sum(a, b):
    return a + b

# This function can sum over many POSITIONAL ARGUMENTS
def my_sum(*args):
    result = 0
    # Iterating over the Python args TUPLE
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

# This function concatenates a string
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs DICTIONARY
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# Combined funciton arguments NEED to come in this order: 
#  1. Standard arguments
#  2. *args arguments
#  3. **kwargs arguments

# Unpacking Operators * and **
# * and ** are operators that unpack the values from iterable objects.
# * can be used on any iterable
# ** can only be used on dictionaries
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *middle, last = my_list
print(my_list, *my_list, sep=' | ')
print(first, middle, last, sep='\n')

# Merging lists and dictionaries with * and **
first_list = [1, 2, 3]
second_list = [4, 5, 6]
merged_list = [*first_list, *second_list]
nested_list = [first_list, second_list]
# Dicts
first_dict = {"A": 1, "B": 2}
second_dict = {"C": 3, "D": 4}
merged_dict = {**first_dict, **second_dict}
print(merged_dict)
# WHAT IS RETURNED BY THE ** OPERATOR???
# ** operator is ONLY usable on dictionaries. It returns keys and their 
# corresponding values. As such, this output can only be put into a dict().


# String to list of 1-letter strings
a = [*"RealPython"]
print(a)

