# Tutorial on @decorators
# https://www.datacamp.com/community/tutorials/decorators-python

# @decorators are used to assign new functionality to 
# an already existing object without modifying its structure.

from typing import Callable

# Assign function to a variable
def plus_one(number: float) -> float:
    return number + 1

add_one = plus_one
print(add_one(5))

# Define a function inside a function
def plus_one(number: float) -> float:
    def add_one(number: float) -> float:
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))

# Passing a function as an argument to another function
# Type hints: Callable[[Arg1Type, Arg2Type], ReturnType]
def plus_one(number: float) -> float:
    return number + 1

def function_call(function: Callable[[float], float]) -> float:
    number_to_add = 8
    result = function(number_to_add)
    return result

print(function_call(plus_one))

# Functions returning other functions
# f: Callable[[int], int] = lambda x: x * 2
def hello_function() -> Callable[[], str]:
    def say_hi() -> str:
        return "Hi"
    return say_hi

hello = hello_function()
print(hello())

# Nested functions have access to the enclosing function's variables
def print_message(message: str) -> None:
    "Enclosing function"
    def message_sender() -> None:
        "Nested function"
        print(message)

    message_sender()

print_message('Maria es guapisima')

# WHAT ON EARTH ARE WRAPPERS