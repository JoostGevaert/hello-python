import os


import pandas as pd
import concurrent.futures

from time import sleep

from pprint import pprint

import a_immutable_data as imm, b_filter as fltr, c_map, d_reduce as rdc
import e_multiprocess as mltprc

### 1: immutable data structures ### 
scntsts_man = imm.scntsts_manual()
df = imm.load_from_csv()
scntsts_pd = imm.scntsts_pandas(df)

pprint(scntsts_man)
pprint(scntsts_pd)
print(type(scntsts_man), type(scntsts_pd))
print(type(scntsts_man[0]), type(scntsts_pd[0]))


### 2: filter() function OR list comprehension ###
fs_man = fltr.scntst_filter(scntsts_man, fltr=2)
fs_pd = fltr.scntst_filter(scntsts_pd, fltr=2)

pprint(fs_man)
pprint(fs_pd)
print(type(fs_man), type(fs_pd))
print(type(fs_man[0]), type(fs_pd[0]))


### 3: map() function OR generator expression ###
ms_man = c_map.scntst_map(scntsts_man)
ms_pd = c_map.scntst_map(scntsts_pd)

pprint(ms_man)
pprint(ms_pd)
print(type(ms_man), type(ms_pd))
print(type(ms_man[0]), type(ms_pd[0]))


### 4: reduce function ###
print(f'Total age for manual Tuple: {rdc.scntst_tot_age(scntsts_man)}')
print(f'Total age for Pandas Tuple: {rdc.scntst_tot_age(scntsts_pd)}')
scntsts_by_field_man = rdc.scntsts_by_field(scntsts_man)
scntsts_by_field_pd = rdc.scntsts_by_field(scntsts_pd)

pprint(scntsts_by_field_man)
pprint(scntsts_by_field_pd)
print(type(scntsts_by_field_man), type(scntsts_by_field_pd))
print(type(scntsts_by_field_man['math']), type(scntsts_by_field_pd['math']))


### 5 (multiprocessing) & 6 (concurrent.futures) parallel processing ###

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
