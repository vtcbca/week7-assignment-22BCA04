#print last 5 rows
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
#.tail() method print last 5 rows from the dataframe
df.tail()
