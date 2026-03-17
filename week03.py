import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(3))
print(mpg.tail(3))

print(mpg.sort_values('mpg'))