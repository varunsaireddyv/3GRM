import pandas
import os
# print(os.curdir)
orders=[]
df = pandas.read_csv("/home/sai/Desktop/FoodDataSet.csv")
print(type(orders))
catageries = df["Food_Category"].unique()
print(type(catageries[0]))

a=1
while a == 1 :
    x=1
    for i in catageries :
        print(x, i)
        x=x+1
    CatIndex = input("please select the id: ")

    if CatIndex == 'exit' :
        break
    else :
        Bool_Items=df["Food_Category"]==catageries[int(CatIndex)-1]
        Items=df[Bool_Items]
        y=1
        for i in Items['Item_Name'] :
            print(y, i)
            y=y+1
        Item_index=input("please select the item id:\n")
        orders.append(Items.iloc[int(Item_index)-1, :])
Total_Calories=0
for order in orders:
    print(order[12])
    Total_Calories=Total_Calories + order[12]
print('this is the total amount of calories: ' , Total_Calories)

    
