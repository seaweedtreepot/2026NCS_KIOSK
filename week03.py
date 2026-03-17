import pandas as pd
import numpy as np

items = {'a':[100, 90, 80],
         'b':[70,85, 95],
         'c':[60,95, 100]
         }

df_items = pd.DataFrame(items,index=[1,2,3])
print(df_items)
