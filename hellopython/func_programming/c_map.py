from collections import namedtuple
from typing import Tuple, NamedTuple
from datetime import datetime


### 3: map() function OR generator expression ###
# map(fuction: lambda parameter_list: expression, sequence: iterable) -> iterator:

def scntst_map(scientists: Tuple[NamedTuple]) -> Tuple[NamedTuple]:
    # Define named tuple to which names and ages will be mapped
    name_and_age = namedtuple('name_and_age', ['name', 'age'])
    # Map first- last name AND calculated "age" to named tuple
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
        for x in scientists
    )

    return names_and_ages

if __name__ == '__main__':
    import a_immutable_data as imm
    from pprint import pprint
    
    ms = scntst_map(imm.scntsts_manual())
    pprint(ms)
    print(type(ms))
    print(type(ms[0]))
