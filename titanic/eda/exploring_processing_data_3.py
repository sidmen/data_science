from eda_default_parameters import *

'''to find if there are missing values'''
# print(df.info())


###########################################"""Feature: Embarked"""#################################################


'''extract rows with Embarked as Null'''
df[df.Embarked.isnull()]

""" you would find that there are 2 rows missing values for Embarked column. Also PEOPLE IN BOTH THE ROWS HAVE SURVIVED
    now we need to find the most Embarked value using value_counts()"""

df.Embarked.value_counts()

"""you would observe that the Southamton is the most Embarked place
   lets also analyse which Embarked point has got higher survival count using crosstab of Survived and Embarked"""

pd.crosstab(df[df.Survived != -888].Survived, df[df.Survived != -888].Embarked)

"""you would observe that the Southamton Embarked point has got more survivors,
   thus we can replace/impute the missing Embarked value with Southamton i.e., 'S' """

'''use either of the following to impute the missing values'''
df.loc[df.Embarked.isnull(), 'Embarked'] = 'S'
# or using the fillna function which is a panda function for the purpose of imputation.
df.Embarked.fillna('S', inplace=True)
""" Here, 'inplace=True' will replace the values in the original table,
    whereas, 'inplace=False' will create a new table with the imputation"""

###########################################"""Feature: Fare"""#################################################

'''to find if there are missing values'''
# print(df.info())

'''extract rows with Fare as Null'''
df[df.Fare.isnull()]

"""you would find that there's a missing Fare value for a person Embarked at S with PClass 3
   let's find out the median of Fares of people Embarked at S and PClass 3"""

median_fare = df.loc[(df.Pclass == 3) & (df.Embarked == 'S'), 'Fare'].median()

"""now fill out the missing value using fillna"""

df.Fare.fillna(median_fare, inplace=True)


###########################################"""Feature: Age"""#################################################

'''to find if there are missing values'''
# print(df.info())

'''extract rows with Age as Null'''
df[df.Age.isnull()]

"""Note: To set te max num of rows to be displayed => pd.options.display.max_rows = 15 """

# use the .transform('median') function to compute the median age of each and every passenger, while just .median will give the median age of all male and all female
age_sex_median = df.groupby(['Sex']).Age.transform('median')
# print(age_sex_median)


"""Lets find the missing age based on the Title of the person. Mister for old perosn and Master for a child"""

'''Function to extract Title from name Eg. Menon, Mr. Sidharth, here we need to extract Mr as mr'''


def GetTitle(name):
    first_name_with_title = name.split(',')[1]
    title = first_name_with_title.split('.')[0]
    title = title.strip().lower()
    return title


'''use map function to apply the function on each Name value row i'''
df.Name.map(lambda x: GetTitle(x))  # alternatively you can use: df.Name.map(GetTitle)

'''use the .unique() function to get the unique values of the output'''
df.Name.map(lambda x: GetTitle(x)).unique()


'''add new column Title'''
df['Title'] = df.Name.map(lambda x: GetTitle(x))

'''replace missing age values'''
title_age_median = df.groupby('Title').Age.transform('median')
df.Age.fillna(title_age_median, inplace=True)


###############################################################   OUTLIERS   ######################################################
# view https://app.pluralsight.com/player?course=python-data-science&author=abhishek-kumar&name=python-data-science-m6&clip=9&mode=live


###########################################################   FEATURE ENGINEERING   ################################################
"""         Process of transforming raw data to better representative features in order to create better predictive models          """

"""Feature : Age State (Adult or Child)"""

'''AgeState based on Age'''
df['AgeState'] = np.where(df['Age'] >= 18, 'Adult', 'Child')

'''AgeState Counts'''
df['AgeState'].value_counts()

'''crosstab to find the survivors based on AgeState'''
pd.crosstab(df[df.Survived != -888].Survived, df[df.Survived != -888].AgeState)
####################
####################
"""Feature: Family Size"""
df['FamilySize'] = df.Parch + df.SibSp + 1   # See Parch and SibSp in csv file. 1 is self

'''further explore this family with max family members'''
df.loc[df.FamilySize == df.FamilySize.max(), ['Name', 'Survived', 'FamilySize', 'Ticket']]
'''create crosstab'''
pd.crosstab(df[df.Survived != -888].Survived, df[df.Survived != -888].FamilySize)
####################
####################
"""Feature: IsMother"""
'''a lady aged more than 18 who has Parch > 0 and is married (not Miss)'''
df['IsMother'] = np.where(((df.Sex == 'female') & (df.Parch > 0) &
                           (df.Age > 18) & (df.Title != 'Miss')), 1, 0)

'''create crosstab'''
print(pd.crosstab(df[df.Survived != -888].Survived, df[df.Survived != -888].IsMother))


###########################################################   CATEGORIAL FEATURE ENCODING   ################################################
"""                                               converting categorical feature to numerical feature                                   """

df['IsMale'] = np.where(df.Sex == 'male', 1, 0)

""" drop and reorder columns """
# drop columns
df.drop(['Cabin', 'Name', 'Ticket', 'Parch', 'SibSp', 'Sex'], axis=1, inplace=True)
# reorder columns
columns = [column for column in df.columns if column != 'Survived']
columns = ['Survived'] | columns
df = df[columns]

"""Save Processed Dataset"""
processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
write_train_path = os.path.join(processed_data_path, 'train.csv')
write_test_path = os.path.join(processed_data_path, 'test.csv')
# train data
df.loc[df.Survived != -888].to_csv(write_train_path)
# test data
columns = [column for column in df.columns if column != 'Survived']
df.loc[df.Survived == -888, columns].to_csv(write_test_path)
