#Display only odd index number column record.
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
print(df.loc[1::2])
