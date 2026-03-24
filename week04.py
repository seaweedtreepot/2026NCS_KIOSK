import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(3))
print(mpg.iat[1, 8])