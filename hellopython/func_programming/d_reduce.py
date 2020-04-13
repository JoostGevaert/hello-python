from typing import Tuple, NamedTuple, Dict, List
from functools import reduce
from collections import defaultdict

import c_map

### 4: reduce function ###
# reduce(function: lambda inputs: expression, squence: iterable, initial: value) -> value:

def scntst_tot_age(scientists: Tuple[NamedTuple]) -> int:
    names_and_ages = c_map.scntst_map(scientists)
    # With the reduce function
    total_age = reduce(
        lambda acc, val: acc + val.age, # inputs (accumulator & age value): expression
        names_and_ages,   # Iterable
        0)                              # Initial value for accumulator

    # The more pythonic way
    total_age = sum(x.age for x in names_and_ages)

    return total_age

# For more complicated applications the reduce() function IS handy
def reducer(acc, val):
    acc[val.field].append(val.first_name + " " + val.last_name)
    return acc

def scntsts_by_field(scientists: Tuple[NamedTuple]) -> Dict[str, List]:
    scientists_by_field = dict(reduce(
        reducer,
        scientists,
        defaultdict(list)
    ))
    return scientists_by_field

if __name__ == '__main__':
    import a_immutable_data as imm
    from pprint import pprint
    
    total_age = scntst_tot_age(imm.scntsts_manual())
    print(total_age)
    scientists_by_field = scntsts_by_field(imm.scntsts_manual())
    pprint(scientists_by_field)
    print(type(scientists_by_field))
    print(type(scientists_by_field['math']))