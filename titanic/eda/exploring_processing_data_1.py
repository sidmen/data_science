
from eda_default_parameters import *

# raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')


# print(type(train_df))

# print(train_df.info())

# print(test_df.info())

# print(test_df.info())

# print(df.info())

'''use .head() to get top 5 rows or head(n) to get top n rows'''
# print(df.head())

'''use .tail() to get bottom 5 rows or tail(n) to get bottom n rows'''
# print(df.tail())

'''column selection using dot'''
df.Name
# or
df['Name']


'''indexing : use loc for label based indexing'''
'''all columns'''
df.loc[5:10, ]
'''selecting column range'''
df.loc[5:10, 'Age': 'Pclass']
'''select discrete columns'''
df.loc[5:10, ['Survived', 'Fare', 'Embarked']]


'''indexing: use iloc for position based indexing'''
df.iloc[5:10, 3:8]

'''filter rows based on condition'''
male_passengers = df.loc[df.Sex == 'male', :]
# print('Number of male passengers: {0}'.format(len(male_passengers)))
'''use & or | operators to build complex logic'''
male_passengers_first_class = df.loc[((df.Sex == 'male') & (df.Pclass == 1)), :]
# print('Number of male passengers in first class: {0}'.format(len(male_passengers_first_class)))


'''use .describe() to get statistics of all numeric columns'''
df.describe()


''' NUMERICAL FEATURES (manual - df.describe will fetch all the below automatically)'''
'''centrality measures'''
# print('Mean fare: {0}'.format(df.Fare.mean()))
# print('Median fare: {0}'.format(df.Fare.median()))

'''dispersion measures'''
# print('Min fare: {0}'.format(df.Fare.min()))
# print('Max fare: {0}'.format(df.Fare.max()))
# print('Fare range: {0}'.format(df.Fare.max() - df.Fare.min()))
# print('25 percentile: {0}'.format(df.Fare.quantile(.25)))
# print('50 percentile: {0}'.format(df.Fare.quantile(.50)))
# print('75 percentile: {0}'.format(df.Fare.quantile(.75)))
# print('Variance fare: {0}'.format(df.Fare.var()))
# print('Standard deviation fare: {0}'.format(df.Fare.std()))

'''box-whisker plot'''
# df.Fare.plot(kind='box')
# plt.show()

'''use .describe(include='all') to get statistics for all columns including non-numeric ones'''
df.describe(include='all')

'''categorial column: Counts'''
df.Sex.value_counts()

'''apply on other columns'''
df[df.Survived != -888].Survived.value_counts()

'''count: Passenger class'''
df.Pclass.value_counts()

'''visualize counts'''
# df.Pclass.value_counts().plot(kind='bar')
# plt.show()

'''title: to set title, color: to set color, rot: to rotate labels'''
# df.Pclass.value_counts().plot(kind='bar', rot=1, title='Class wise passenger count', color='m')
# plt.show()


'''last line'''
