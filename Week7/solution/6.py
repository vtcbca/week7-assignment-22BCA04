#Add 2 row after 3rd row.
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)

#to know the length of the dataframe
len(df)

df.loc[2.5]=[15,'Music Player',5000,5000,5000,5000,5000,5000,30000]
df.loc[2.6]=[16,'Sound System',6000,6000,6000,6000,6000,6000,36000]
df=df.sort_index().reset_index(drop=True)
print(df)
