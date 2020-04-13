import os
from typing import Tuple, NamedTuple
from collections import namedtuple
from datetime import datetime
from time import time, sleep
from pprint import pprint

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import pathos       # Apparently uses impractical "multiprocessing" API

import a_immutable_data as imm

# MULTIPROCESSING AND CONCURRENT.FUTURES HAVE ISSUES WITH PICKLING
# Options for solving the issues:
# 1. Use data formats that CAN be pickled: 
#       e.g. df.itertuples(name=None) -> Tuple, instead of NamedTuple
# 2. Use other multiprocess libraries
#   a. Dask - library for parallel computing in Python - has Pandas, Numpy, Scikit-learn API's
#   b. pathos - uses "dill" to pickle, dill is more versatile

# Note from Dask website:
# "If you are looking to manage a terabyte or less of tabular CSV or JSON data, 
# then you should forget both Spark and Dask and use Postgres or MongoDB."


scientist = namedtuple(
    'scientist', ['first_name', 'last_name', 'field', 'born', 'nobel_prize']
)
scientists = (
    scientist(first_name='Ada', last_name='Lovelace', field='math', born=1815, nobel_prize=False),
    scientist(first_name='Emmy', last_name='Noether', field='math', born=1882, nobel_prize=False),
    scientist(first_name='Marie', last_name='Curie', field='physics', born=1867, nobel_prize=True),
    scientist(first_name='Tu', last_name='Youyou', field='chemistry', born=1938, nobel_prize=True),
    scientist(first_name='Ada', last_name='Yonath', field='chemistry', born=1939, nobel_prize=True),
    scientist(first_name='Vera', last_name='Rubin', field='astronomy', born=1928, nobel_prize=False),
    scientist(first_name='Sally', last_name='Ride', field='physics', born=1951, nobel_prize=False),
)

def transform(x):
    print(f'Processing record {x.first_name}')
    sleep(1)
    result = {'name': x.first_name, 'age': 2020 - x.born}
    print(f'Done rocessing record {x.first_name}')
    return result

# Sequential run
start_time = time()
result = tuple(map(transform, scientists))
elapsed_time = time() - start_time

print(f'It took {elapsed_time:.2f} sec to sequentially produce:')
pprint(result)

# With multiprocessing
start_time = time()
pool = multiprocessing.Pool()
result = tuple(pool.map(transform, scientists))
elapsed_time = time() - start_time

print(f'It took {elapsed_time:.2f} seconds with multiprocessing to produce:')
pprint(result)

# With concurrent.futures
start_time = time()
with ProcessPoolExecutor() as executor:
    result = tuple(executor.map(transform, scientists))
elapsed_time = time() - start_time

print(f'It took {elapsed_time:.2f} seconds with multiprocessing to produce:')
pprint(result)


### ABOVE THIS LINE WAS DONE ACCORDING TO THE TUTORIAL. ###
####################################################################################
### Below does not work, because of pickling problems. ###
## With pathos.multiprocessing


# scntsts_pd = imm.load_from_csv()

# start_time = time()
# pool = pathos.multiprocessing.Pool()
# result = tuple(pool.map(transform, scntsts_pd))
# elapsed_time = time() - start_time

# print(f'It took {elapsed_time:.2f} seconds with multiprocessing to produce:')
# pprint(result)





# def my_transform(x: Tuple[NamedTuple]) -> NamedTuple:
#     name = str(x.first_name + " " + x.last_name).lower()
#     print(f'Process {os.getpid()} working record: {name}')
#     # sleep(1)
#     name_and_age = namedtuple('name_and_age', ['name', 'age'])
#     n_a_a = name_and_age(
#         name=name.title(), 
#         age=datetime.now().year - x.born,
#     )
#     print(f'Process {os.getpid()} done processing record: {name}')
#     return n_a_a







