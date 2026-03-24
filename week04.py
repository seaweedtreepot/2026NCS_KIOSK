import seaborn as sns
#cars that made in eu with mpg is higher than 30
#but, only print name of the car, mpg, country,
#And, update the downloaded-origin-data
mpg = sns.load_dataset('mpg')
#print(mpg.info())

mpg = (mpg.drop(columns=['cylinders', 'displacement','horsepower','weight','acceleration','model_year']))
print(mpg.info())
mpg = mpg[['mpg','origin','name']].query('origin == "europe" and mpg >= 30').sort_values('mpg',ascending=False)

#print(mpg)