from collections import namedtuple
import pandas as pd

# tuple of named tuples
nmd_tpl = namedtuple('Pandas', ['Index', 'col1', 'col2'])
tpl_nmd_tpl1 = (nmd_tpl(Index=0, col1=1, col2=3),
                nmd_tpl(Index=1, col1=2, col2=4))
print(tpl_nmd_tpl1, type(tpl_nmd_tpl1[0]))

# tuple of named tuples from pd.dataframe
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
tpl_nmd_tpl2 = tuple(df.itertuples())
print(tpl_nmd_tpl2, type(tpl_nmd_tpl2[0]))