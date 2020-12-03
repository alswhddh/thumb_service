import os
import sqlite3
import pandas as pd
from pandas import Series, DataFrame

#print(os.getcwd())

df = pd.read_pickle("./thumb/nail/static/data/result.pkl")
con = sqlite3.connect("./thumb/thumbnail.db")
df.to_sql('thumbnail',con,if_exists='replace') # arg chunksize=1000