import seaborn as sns
#cars that made in eu with mpg is higher than 30
#but, only print name of the car, mpg, country,
mpg = sns.load_dataset('mpg')

ans = mpg[['mpg','origin','name']].query('origin == "europe" and mpg >= 30').sort_values('mpg',ascending=False)

print(ans)