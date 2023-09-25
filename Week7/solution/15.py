#Display alternate row
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
print(df.loc[::2])
