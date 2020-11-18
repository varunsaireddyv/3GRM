import pandas
import os
# print(os.curdir)
orders=[]
df = pandas.read_csv("/home/sai/Desktop/FoodDataSet.csv")
print(type(orders))
catageries = df["Food_Category"].unique()
a=1
while a == 1 :
    x=1
    for i in catageries :
        print(x, i)
        x=x+1
    CatIndex = input("please select the id: ")

    if CatIndex == 'exit' :
        break
    elif CatIndex == '1' :
        bb=df["Food_Category"]=="Beverages"
        bev=df[bb]
        y=1
        for i in bev['Item_Name'] :
            print(y, i)
            y=y+1
        Item_index=input("please select the item id:\n")
        if Item_index == '1' :
            orders.append(bev.iloc[0, :])
        elif Item_index == '2' :
            orders.append(bev.iloc[1, :])
        elif Item_index == '3' :
            orders.append(bev.iloc[2, :])
        elif Item_index == '4' :
            orders.append(bev.iloc[3, :])
        elif Item_index == '5' :
            orders.append(bev.iloc[4, :])
        elif Item_index == '6' :
            orders.append(bev.iloc[5, :])
    elif CatIndex == '2' :
        sab=df["Food_Category"]=="Sandwiches"
        sandwhich=df[sab]
        z=1
        for i in sandwhich['Item_Name'] :
            print(z, i)
            z=z+1       
        Item_index2=input('please select the item id:\n')
        if Item_index2 == '1' :
            orders.append(sandwhich.iloc[0, :])
        elif Item_index2 == '2':
            orders.append(sandwhich.iloc[1, :])
        elif Item_index2 == '3':
            orders.append(sandwhich.iloc[2, :])
        elif Item_index2 == '4':
            orders.append(sandwhich.iloc[3, :])
        elif Item_index2 == '5':
            orders.append(sandwhich.iloc[4, :])  
Total_Calories=0
for order in orders:
    print(order[12]) 
    Total_Calories=Total_Calories + order[12]
print('this is the total amount of calories:-' , Total_Calories)

    
