#print only product Name
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
df['Product Name']
