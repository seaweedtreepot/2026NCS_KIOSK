import pandas as pd
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.info())

# mpg_fill = mpg.fillna(0)
# print(mpg_fill.info())

# mpg.dropna(subset=['horsepower'],inplace=True)
# print(mpg.info())

med = mpg['horsepower'].median()

mpg_filled = mpg.copy()
mpg_filled['horsepower'] = mpg_filled['horsepower'].fillna(med)

print(mpg_filled.info())