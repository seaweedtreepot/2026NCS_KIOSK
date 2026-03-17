import pandas as pd
import numpy as np

# items = {'a':[100, 90, 80],
#          'b':[70,85, 95],
#          'c':[60,95, 100]
#          }

items = [
    [100,95,70],
    [75,65,35],
    [100,30,20]
]
df_items = pd.DataFrame(items, index=[1,2,3],columns=['a','b','c'])
print(df_items)

df_items_melt = (pd.melt(df_items).rename(columns={'variable':'var','value':'val'}).query('val >= 75'))
print(df_items_melt)