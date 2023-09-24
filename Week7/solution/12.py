#print sell of january month with product id and product name
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
data=df[(df["January"]>5000) & (df["February"]>8000)][['Product No','Product Name']]
print(data)
