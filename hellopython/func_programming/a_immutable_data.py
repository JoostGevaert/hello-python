from pathlib import Path
import yaml
from collections import namedtuple
from typing import Tuple, NamedTuple
import pandas as pd
from pprint import pprint

### 1: immutable data structures ### 
# Manually defining the NamedTuples inside the Tuple
def scntsts_manual() -> Tuple[NamedTuple]:
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
    return scientists


def load_from_csv() -> pd.DataFrame:
    # Load configuration
    base_dir = Path.cwd().parent.parent
    with open("../conf.yml") as file:
        CONF = yaml.safe_load(file)
    data_path = base_dir.joinpath(Path(CONF['scientists']['filepath']))

    # Read .csv as pandas DataFrame
    df = pd.read_csv(data_path)
    # map Nobel Prize yes/no to Boolean True/False
    df['nobel_prize'] = df['nobel_prize'].map(dict(yes=True, no=False))
    return df

# Constructing a Tuple(NamedTuple) from Pandas.DataFrame
def scntsts_pandas(df: pd.DataFrame) -> Tuple[NamedTuple]:
    scientists = tuple(df.itertuples(name='scientist', index=False))
    return scientists

if __name__ == '__main__':
    scntsts_man = scntsts_manual()
    pprint(scntsts_man)
    print(type(scntsts_man))
    print(type(scntsts_man[0]))

