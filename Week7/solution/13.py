#print record in sorting order of product name.
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
sorted_name=df.sort_values(by='Product Name')
print(sorted_name)
