import seaborn as sns
import pandas as pd
#cars that made in eu with mpg is higher than 30
#but, only print name of the car, mpg, country,
#And, update the downloaded-origin-data
mpg = sns.load_dataset('mpg')

group_mpg = pd.DataFrame(mpg.groupby(by='cylinders'))
print(group_mpg)
#print(mpg.groupby(by='origin'))