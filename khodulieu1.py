import pandas as pd


df = pd.read_csv('D:\\US Accident Smaller.csv')

df_filled = df.fillna("null")

df_filled.to_csv('D:\\US Accident Smallers.csv', index=False)
