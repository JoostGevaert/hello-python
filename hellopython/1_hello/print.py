### Very basic Python ###
import os
import sys

### print() tutorial |  Real Python ###
# build-in python types
print(42)                            # <class 'int'>
print(3.14)                          # <class 'float'>
print(1 + 2j)                        # <class 'complex'>
print(True)                          # <class 'bool'>
print([1, 2, 3])                     # <class 'list'>
print((1, 2, 3))                     # <class 'tuple'>
print({'red', 'green', 'blue'})      # <class 'set'>
print({'name': 'Alice', 'age': 42})  # <class 'dict'>
print('hello')                       # <class 'str'>

# sep=    keyword argument (kwarg)
# Specify the seperator between positional arguments in print()
print('', 'home', 'joost', 'Documents', 'git', 'hello_python', sep='/') #path
print('My name is', os.getlogin(), 'and I am', 24, sep=',') # to csv

# end=    kwarg
# Specify what the newline looks like between 2 seperate print() calls
# or use it to make sure that \n doesn't start a new line.
print('Checking file integrity...', end='')
# (...) check the integrity of the file here
print('ok') # prints 'ok' on the same line, due to end=''


## Standard Streams ##
print(sys.stdin, '| File Descriptor:', sys.stdin.fileno(), '\n',
     sys.stdout, '| File Descriptor:', sys.stdout.fileno(), '\n',
     sys.stderr, '| File Descriptor:', sys.stderr.fileno())