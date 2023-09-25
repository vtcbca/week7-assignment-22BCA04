#print First 5 rows
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
#.head() method print first 5 rows from the dataframe
df.head()
