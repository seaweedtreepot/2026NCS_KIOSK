import seaborn as sns
import pandas as pd
mpg = sns.load_dataset('mpg')
#print(mpg.head(3))
#print(mpg.iloc[:, [0,1]])

#print (mpg.loc[:,'model_year':'origin'])
print(mpg.at[4,'A'])