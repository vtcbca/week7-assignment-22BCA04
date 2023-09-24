import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
df.columns=['Product No','Product Name','January','February','March','April','May','June']
print(df)


