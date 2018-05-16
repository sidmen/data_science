import pandas as pd
import numpy as np
import os
from matplotlib import *
import matplotlib.pyplot as plt

raw_data_path = os.getcwd() + '\\titanic\\sid_notes\\eda'
train_file_path = os.path.join(raw_data_path, 'train.csv')
test_file_path = os.path.join(raw_data_path, 'test.csv')

'''read the data with all default parameters'''
train_df = pd.read_csv(train_file_path, index_col='PassengerId')
test_df = pd.read_csv(test_file_path, index_col='PassengerId')

'''add Survived column for test_dff'''
test_df['Survived'] = -888  # some arbitrary value

'''axis=0 concats row-wise | axis=1 concats column-wise'''
df = pd.concat((train_df, test_df), axis=0)
