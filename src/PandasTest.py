# coding=utf-8
import pandas as pd
df = pd.read_csv('C://Users//lx201//Desktop//meshpair_metric20//12.csv','utf-8','\t',header=None)
print(df.ix[[0],])