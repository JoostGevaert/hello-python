from typing import Tuple, NamedTuple


### 2: filter() function OR list comprehension ###
# Apply filter function on tuple of scientists
def nobel_filter(x: Tuple[NamedTuple]) -> NamedTuple:
    return x.nobel_prize is True

def physics_filter(x: Tuple[NamedTuple]) -> NamedTuple:
    return x.field == 'physics'

def scntst_filter(scientists: Tuple[NamedTuple], fltr=1) -> Tuple[NamedTuple]:
    if fltr == 1:
        fs = tuple(filter(nobel_filter, scientists))
    elif fltr == 2:
        fs = tuple(filter(physics_filter, scientists))
    elif fltr == 3:     # with an inline lambda function
        fs = tuple(filter(lambda x: x.field == 'physics' and x.nobel_prize is True, scientists))
    else:               # with LIST COMPREHENSION, this is the more PYTHONIC way
        # "give me all x, where x is in scientists if"
        fs = tuple(x for x in scientists if x.field == 'physics' and x.nobel_prize is True)
    return fs

if __name__ == '__main__':
    import a_immutable_data as imm
    from pprint import pprint
    
    fs = scntst_filter(imm.scntsts_manual(), fltr=4)
    pprint(fs)
    print(type(fs))
    print(type(fs[0]))