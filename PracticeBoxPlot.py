import pandas as pd
import matplotlib as mp

df = pd.read_csv('./tips.csv')
print(df.head())

df.boxplot(column = ['total_bill'], rot = 0)