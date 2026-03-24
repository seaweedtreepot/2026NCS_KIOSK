import pandas as pd

def squares(n) :
    return n * n
items = {'a':[100, 90, 80],
         'b':[70,85, 95],
         'c':[60,95, 100]
         }
df_items = pd.DataFrame(items,index=[1,2,3])
print(df_items)
print(df_items.apply(squares))

print(df_items.apply(lambda n : n * n))