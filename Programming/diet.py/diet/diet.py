import pandas
import os
# print(os.curdir)
order=[]
df = pandas.read_csv("/home/sai/Desktop/FoodDataSet.csv")
print(type(cart))
catageries = df["Food_Category"].unique()
x=1
for i in catageries :
    print(x, i)
    x=x+1
CatIndex = input("please select the id:\n")
if CatIndex == '1' :
    bb=df["Food_Category"]=="Beverages"
    bev=df[bb]
    y=1
    for i in bev['Item_Name'] :
        print(y, i)
        y=y+1
    Item_index=input("please select the item id:\n")
    if Item_index == '1' :
        order.append('French Vanilla Cappuccino')
    elif Item_index == '2' :
        order.append('Peppermint Mocha')    
    elif Item_index == '3' :
        order.append(' Pumpkin Spice Latte')
    elif Item_index == '4' :
        order.append('Caramel Macchiato')
    elif Item_index == '5' :
        order.append('Hot Chocolate')    
    elif Item_index == '6' :
        order.append('Cappuccino') 
elif CatIndex == '2' :
    sab=df["Food_Category"]=="Sandwiches"
    sal=df[sab]
    z=1
    for i in sal['Item_Name'] :
        print(z, i)
        z=z+1       
    Item_index2=input('please select the item id:/n')
    if Item_index2 == '1' :
        cart.append('Southwest Turkey Sandwich')
    elif Item_index2 == '2':
        cart.append('7 Select Go!Smart Turkey Sandwich')    
    elif Item_index2 == '3':
        cart.append('Chicken Salad Sandwich')
    elif Item_index2 == '4':
        cart.append('Italian Melt')
    elif Item_index2 == '5':
        cart.append('Chicken Fajita Rollup')
print(cart)        
    