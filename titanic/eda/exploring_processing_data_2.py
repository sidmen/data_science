from eda_default_parameters import *

'''use kind=hist to create histogram'''
# df.Age.plot(kind='hist', title='histogram of Age', color='c')

'''use bins to add or remove bins'''
# df.Age.plot(kind='hist', title='histogram of Age', color='y', bins = 20)   # the last semicolon is to avoid unnecessary line saying about type of plot in output

'''use kde for density plot'''
# df.Age.plot(kind='kde', title='Density plot for Age', color='c')

'''histogram for fare'''
# df.Fare.plot(kind='hist', title='histogram for Fare', color='c', bins=20)

'''use .skew() to measure skewness'''
# skewness_for_age = df.Age.skew()
# skewness_for_fare = df.Fare.skew()
# print('Skewness for age: {0:.2f}'.format(skewness_for_age))
# print('Skewness for fare: {0:.2f}'.format(skewness_for_fare))

'''use scatter plot for bivariate distribution'''
# df.plot.scatter(x='Age', y='Fare', color='c', title='scatter plot: Age vs Fare', alpha=0.1)   # alpha is opacity of the scatter dots
# df.plot.scatter(x='Pclass', y='Fare', color='c', title='Scatter plot: Passenger class vs Fare', alpha=0.15)

'''use groupby function to group'''
df.groupby(['Sex']).Age.median()
group_by_single_column = df.groupby(['Pclass']).Age.median()
group_by_multiple_columns = df.groupby(['Pclass'])['Fare', 'Age'].median()
# print(group_by_multiple_columns)

'''use .agg function to apply aggregations'''
aggregation = df.groupby(['Pclass']).agg({'Fare': 'mean', 'Age': 'median'})
# print(aggregation)

'''more complicated aggregations'''
aggregations_dict = {
    'Fare': {  # work on the 'Fare' column
        'mean_Fare': 'mean',
        'median_Fare': 'median',
        'max_Fare': max,
        'min_Fare': np.min
    },
    'Age': {
        'median_Age': 'median',
        'min_Age': min,
        'max_Age': max,
        'range_Age': lambda x: max(x) - min(x)
    }
}
aggregations = df.groupby(['Pclass']).agg(aggregations_dict)
# print(aggregations)

df.groupby(['Pclass', 'Embarked']).Fare.median()


'''crosstab'''
pd.crosstab(df.Sex, df.Pclass)
# pd.crosstab(df.Sex, df.Pclass).plot(kind='bar')

'''pivot table'''
# the below will calculate the mean value of Ages based on [passenger class and their gender]:
df.pivot_table(index='Sex', columns='Pclass', values='Age', aggfunc='mean')
# the above can be achieved by below - unstack() function to order the output:
df.groupby(['Sex', 'Pclass']).Age.mean().unstack()
