#Add 2 row at the end.
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
#to know the length of the dataframe
len(df)

df.loc[12]=[13,'Camera',4500,6000,10000,9500,8500,8000]
df.loc[13]=[14,'Head-phone',6500,7200,3600,4500,9000,6000]
print(df)
