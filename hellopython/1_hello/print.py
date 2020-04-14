### Very basic Python ###
import os
import sys
import io

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
# stdin: Standard in; Keyboard | stdout: Standard out; terminal
# stderr: Standard error output; terminal
# All can be redirected to a file, also the input can come from a file
# e.g. python hello.py > file.txt | all normal output is redirected to file.txt
print(sys.stdin, '| File Descriptor:', sys.stdin.fileno(), '\n',
     sys.stdout, '| File Descriptor:', sys.stdout.fileno(), '\n',
     sys.stderr, '| File Descriptor:', sys.stderr.fileno())

# Redirecting the output for a single print() call:
# Note that this will make the code immune to stream redirection from terminal
with open('file.txt', mode='w') as file_object:
    print('hello world', file=file_object)

# Storing output in a fake file. Apparently useful for unit testing
fake_file = io.StringIO()
print('hello world', file=fake_file)
fake_file.getvalue()