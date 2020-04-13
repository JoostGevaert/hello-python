import os
from pathlib import Path
from collections import namedtuple, defaultdict
from typing import Tuple, NamedTuple

import yaml
import pandas as pd
import concurrent.futures
from datetime import datetime
from time import sleep
from functools import reduce
from pprint import pprint

# Load configuration
BASE_DIR = Path.cwd().parent
with open("conf.yml") as file:
    CONF = yaml.safe_load(file)
DATA_PATH = BASE_DIR.joinpath(Path(CONF['scientists']['filepath']))

# Read .csv as pandas DataFrame
data = pd.read_csv(DATA_PATH)
# map Nobel Prize yes/no to Boolean True/False
data['nobel_prize'] = data['nobel_prize'].map(dict(yes=True, no=False))
### 1: immutable data structures ### 
# Convert DF to immutable tuple of named tuples
scientists = tuple(data.itertuples(name='scientist', index=False))


### 2: filter() function OR list comprehension ###
# Apply filter function on tuple of scientists
def nobel_filter(x: Tuple[NamedTuple]) -> NamedTuple:
    return x.nobel_prize is True

def physics_filter(x: Tuple[NamedTuple]) -> NamedTuple:
    return x.field == 'physics'

fs = tuple(filter(nobel_filter, scientists))
fs = tuple(filter(physics_filter, scientists))
# OR with an inline lambda function
fs = tuple(filter(lambda x: x.field == 'physics' and x.nobel_prize is True, scientists))
# OR with LIST COMPREHENSION, this is the more PYTHONIC way
# "give me all x, where x is in scientists if"
fs = tuple(x for x in scientists if x.field == 'physics' and x.nobel_prize is True)


### 3: map() function OR generator expression ###
# map(fuction: lambda parameter_list: expression, sequence: iterable) -> iterator:
# Define named tuple to which names and ages will be mapped
name_and_age = namedtuple('name_and_age', ['name', 'age'])

# Map first and last name AND calculated "age" to named tuple
names_and_ages = tuple(map(
    lambda x: name_and_age(
        name=str(x.first_name + " " + x.last_name).upper(), 
        age=datetime.now().year - x.born,
    ),
    scientists
))

# OR with GENERATOR EXPRESSION, this is the more PYTHONIC way
names_and_ages = tuple(
    name_and_age(
        name=(x.first_name + " " + x.last_name).capitalize(),
        age=datetime.now().year - x.born,
    )
    for x in scientists)


### 4: reduce function ###
# reduce(function: lambda inputs: expression, squence: iterable, initial: value) -> value:
total_age = reduce(
    lambda acc, val: acc + val.age, # inputs (accumulator & age value): expression
    names_and_ages,                 # Iterable
    0)                              # Initial value for accumulator

# OR
total_age = sum(x.age for x in names_and_ages)

# For more complicated applications the reduce() function IS handy
def reducer(acc, val):
    acc[val.field].append(val.first_name + " " + val.last_name)
    return acc

scientists_by_field = reduce(
    reducer,
    scientists,
    defaultdict(list)
)

### 5 (multiprocessing) & 6 (concurrent.futures) parallel processing ###
def transform(x):
    name = str(x.first_name + " " + x.last_name).lower()
    print(f'Process {os.getpid()} working record: {name}')
    # sleep(1)
    name_and_age = namedtuple('name_and_age', ['name', 'age'])
    n_a_a = name_and_age(
        name=name.title(), 
        age=datetime.now().year - x.born,
    )
    print(f'Process {os.getpid()} done processing record: {name}')
    return n_a_a

# Run sequentially
start_time = datetime.now()
names_and_ages = tuple(map(transform, scientists))
elapsed_time = datetime.now() - start_time
print(f'Time taken with sequential run: {elapsed_time}')

def prnt_smthng(x):
    sleep(1)
    print(x)

int_lst = [1, 3, 5, 7, 11, 13, 17, 19, 23]

with concurrent.futures.ProcessPoolExecutor() as exec:
    exec.map(prnt_smthng, data.iterrows())


# Run with multiprocess
# start_time = datetime.now()
# with concurrent.futures.ProcessPoolExecutor() as exec:
#     names_and_ages = exec.map(transform, scientists)
# tuple(names_and_ages)
# elapsed_time = datetime.now() - start_time
# print(f'Time taken to with parallel run: {elapsed_time}')


