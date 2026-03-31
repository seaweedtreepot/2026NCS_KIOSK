import seaborn as sns
import pandas as pd

data = sns.load_dataset('mpg')

#print(data)

df = pd.DataFrame(
    {
        "돈까스" : ['김치','치즈','된장'],
        '쫄면' : ['김치','기본','된장'],
        '붕어빵' : ['팥','김치','슈크림']
    },index = [1,2,3]
)

print (pd.melt(df))