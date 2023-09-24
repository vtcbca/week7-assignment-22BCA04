#Add 2 row after 3rd row.
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
#to know the length of the dataframe
len(df)

df.loc[2.5]=[3.4,'Mobile',4500,6000,10000,9500,8500,8000]
df.loc[2.6]=[3.5,'Head-phone',6500,7200,3600,4500,9000,6000]

df=df.sort_index(),reset_index()
print(df)
