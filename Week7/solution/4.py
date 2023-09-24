#Add column "Total Sell" to count total of all month and "Average Sell"
import pandas as pd
file="c://sqlite3//product.csv"
df=pd.read_csv(file)
df['Total Sell']=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
print(df)


