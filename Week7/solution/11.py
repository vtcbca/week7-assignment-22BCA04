#print sell of january month with product id and product name
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
print(df[['January','Product No','Product Name']])
