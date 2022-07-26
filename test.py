import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split

import sys
sys.path.append("..")
transactions = pd.read_csv('./assets/ratings_Beauty.csv',names=['UserId','ProductId',], header=None)
data = pd.melt(transactions.set_index('UserId')['ProductId'].apply(pd.Series).reset_index(),
             id_vars=['UserId'],
             value_name='ProductId') \
    .dropna().drop(['variable'], axis=1) \
    .groupby(['UserId', 'ProductId']) \
    .agg({'ProductId': 'count'}) \
    .rename(columns={'ProductId': 'purchase_count'}) \
    .reset_index() \
    .rename(columns={'ProductId': 'productId'})

data['productId'] = data['productId'].astype(np.int64)