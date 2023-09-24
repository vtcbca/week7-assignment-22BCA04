#create product.csv file which contain product number,name and selling of january to june month.
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
# 5 product details print in csv file directly
rows=[
    [1,'Keybord',9500,8500,9600,10000,11000,10500],
    [2,'Mouse',5600,4500,3000,5800,6000,6500],
    [3,'Monitor',15000,10500,18000,9000,8500,12000],
    [4,'CPU',36000,30000,45000,40000,32000,31000],
    [5,'Scanner',4500,5600,7500,9000,8500,9500]
     ]

# create empty list to store more 7 product details from user input
l=[] 
for i in range(7):
    n=int(input('Enter Product Id:'))
    name=input('Enter Product Name:')
    jan=int(input('Enter Jan Month Selling:'))
    feb=int(input('Enter Feb Month Selling:'))
    march=int(input('Enter March Month Selling:'))
    april=int(input('Enter April Month Selling:'))
    may=int(input('Enter May Month Selling:'))
    jun=int(input('Enter Jun Month Selling:'))
#   create a list 
    data=[n,name,jan,feb,march,april,may,jun]
    l.append(data)


from csv import writer
file="c://sqlite3//product.csv"

with open(file,"w",newline="")as write_file:
#     create the writer object
    write=writer(write_file)
#     adding header to the csv file
    write.writerow(header)
#     adding 5 record directly
    write.writerows(rows)
#     adding 7 record from user
    write.writerows(l)
    print('successfully file created and data inserted')
