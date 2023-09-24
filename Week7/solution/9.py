#print row 6 to 10
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
#loc[start:stop:step]
#in this here we start from 6 and end to 10.
df.loc[6:10]
